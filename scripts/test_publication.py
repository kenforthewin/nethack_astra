import gzip
import hashlib
import json
from pathlib import Path
import struct
import tempfile
import unittest

import audit
import prepare_publication as publication
import verify_publication


class PublicationTests(unittest.TestCase):
    def test_redaction_and_idempotence(self):
        r = publication.Redactor(['fake-secret-1234'])
        text = 'fake-secret-1234 test+run@example.org /Users/alice/project 192.168.1.25'
        cleaned = r.text(text)
        for private in ('fake-secret-1234', 'example.org', '/Users/alice', '192.168.1.25'):
            self.assertNotIn(private, cleaned)
        self.assertEqual(cleaned, r.text(cleaned))

    def test_ansi_normalization(self):
        r = publication.Redactor(['fake-secret-1234'])
        self.assertTrue(r.findings('fake-\x1b[31msecret-1234'))

    def test_source_exceptions_do_not_change_default_record_redaction(self):
        fixture = 'nethack@us.hardfought.org test+run@example.org /Users/alice 192.168.1.25'
        code = publication.Redactor(allowed=publication.PUBLIC_CODE_LITERALS)
        self.assertEqual(code.text(fixture), fixture)
        self.assertFalse(code.findings(fixture))
        self.assertNotEqual(publication.Redactor().text(fixture), fixture)

    def row(self, kind, data):
        return {'kind': kind, 'data': data, 'seq': 1, 'recorded_at': 'test'}

    def test_unknown_and_tools_fail_closed(self):
        r = publication.Redactor()
        unknown = publication.project(self.row('new_kind', {'body': 'private'}), r)
        self.assertNotIn('private', json.dumps(unknown))
        for typ in ('custom_tool_call', 'custom_tool_call_output', 'function_call_output'):
            item = publication.project(self.row('codex_record', {'source_line': 1,
                'content': {'type': typ, 'input': 'private', 'output': 'private', 'call_id': 'a'}}), r)
            self.assertIn('omitted', item)
            self.assertNotIn('private', json.dumps(item))

    def test_private_analysis_and_injected_context_not_exported(self):
        r = publication.Redactor()
        for c in ({'type': 'message', 'role': 'assistant', 'phase': 'analysis', 'content': [{'type': 'text', 'text': 'secret-thought'}]},
                  {'type': 'message', 'role': 'user', 'content': [{'type': 'input_text', 'text': '<environment_context>private'}]}):
            result = publication.project(self.row('codex_record', {'source_line': 1, 'content': c}), r)
            self.assertIn('omitted', result)
            self.assertNotIn('secret-thought', json.dumps(result))

    def test_sensitive_input(self):
        result = publication.project(self.row('input_requested', {'sensitive': True,
            'input': 'unrecognized-secret', 'screen_before': 'unrecognized-secret'}), publication.Redactor())
        self.assertNotIn('unrecognized-secret', json.dumps(result))

    def test_ttyrec_cross_frame_scan_and_truncation(self):
        frames = [b'secret-', b'123456']
        raw = b''.join(struct.pack('<III', 10 + i, 0, len(b)) + b for i, b in enumerate(frames))
        text, metadata = publication.tty_payload(raw)
        self.assertTrue(publication.Redactor(['secret-123456']).findings(text))
        self.assertEqual(metadata['frames'], 2)
        with self.assertRaises(ValueError):
            publication.tty_payload(raw[:-1])

    def test_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                publication.safe_file(Path(tmp), '../elsewhere')

    def test_verifier_detects_tampering_and_extra_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp); data = b'public'
            (p / 'a.txt').write_bytes(data)
            (p / 'SHA256SUMS').write_text(hashlib.sha256(data).hexdigest() + '  a.txt\n')
            self.assertEqual(verify_publication.verify(p)['files_verified'], 1)
            (p / 'unlisted.txt').write_text('extra')
            with self.assertRaises(ValueError):
                verify_publication.verify(p)
            (p / 'a.txt').write_text('changed')
            with self.assertRaises(ValueError):
                verify_publication.verify(p)

    def test_public_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            row = {'source_seq': 1, 'previous_hash': audit.ZERO}
            head = hashlib.sha256(audit.canonical(row)).hexdigest(); row['hash'] = head
            with gzip.open(p / 'events.jsonl.gz', 'wt') as f:
                f.write(json.dumps(row) + '\n')
            (p / 'manifest.json').write_text(json.dumps({'exported_event_count': 1, 'exported_head_sha256': head}))
            (p / 'SHA256SUMS').write_text('\n'.join(hashlib.sha256(f.read_bytes()).hexdigest() + '  ' + f.name
                                                  for f in sorted(p.iterdir())) + '\n')
            self.assertEqual(verify_publication.verify(p)['events_verified'], 1)


if __name__ == '__main__':
    unittest.main()
