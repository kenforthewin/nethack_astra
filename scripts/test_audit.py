import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import audit
import session


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.runtime = self.directory / 'runtime'
        self.runtime.mkdir()
        self.patches = [patch.object(audit, 'RUNTIME', self.runtime),
                        patch.object(audit, 'secret_values', return_value=['test-secret-123'])]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()
        self.temp.cleanup()

    def test_chain_and_tamper_detection(self):
        audit.append_many(self.directory, [('test', {'x': 1}), ('test', {'x': 2})])
        self.assertEqual(audit.verify(self.directory)['events'], 2)
        file = self.directory / 'events.jsonl'
        file.write_bytes(file.read_bytes().replace(b'"x":1', b'"x":9'))
        with self.assertRaises(RuntimeError):
            audit.verify(self.directory)

    def test_incomplete_tail_fails_closed(self):
        audit.append_many(self.directory, [('test', {})])
        with (self.directory / 'events.jsonl').open('ab') as f:
            f.write(b'{"incomplete":')
        with self.assertRaises(RuntimeError):
            audit.append_many(self.directory, [('test', {})])

    def test_redaction_and_public_email(self):
        self.assertEqual(audit.clean({'password': 'anything'}), {'password': '[REDACTED]'})
        self.assertNotIn('test-secret-123', audit.clean('x test-secret-123 y'))
        self.assertEqual(audit.clean('a+b@example.org', public=True), '[email redacted]')

    def test_no_private_reasoning_or_instructions(self):
        for typ, payload in [
            ('response_item', {'type': 'reasoning', 'text': 'private'}),
            ('response_item', {'type': 'message', 'role': 'assistant', 'phase': 'analysis', 'content': [{'text': 'private'}]}),
            ('response_item', {'type': 'message', 'role': 'developer', 'content': [{'text': 'private'}]}),
            ('compacted', {'message': 'private'}),
            ('event_msg', {'type': 'item_completed', 'item': {'reasoning': 'private'}}),
        ]:
            self.assertIsNone(audit.select_event({'type': typ, 'payload': payload}))
        selected = audit.select_event({'type': 'turn_context', 'payload': {'model': 'gpt-6-astra', 'summary': 'private'}})
        self.assertEqual(selected, {'model': 'gpt-6-astra'})

    def test_public_messages_and_tools_preserved(self):
        for payload in [
            {'type': 'message', 'role': 'assistant', 'phase': 'commentary', 'content': [{'type': 'text', 'text': 'Retreating.'}]},
            {'type': 'custom_tool_call', 'name': 'functions.exec', 'call_id': 'x', 'input': 'tools.example()'},
            {'type': 'custom_tool_call_output', 'call_id': 'x', 'output': 'result'},
        ]:
            self.assertEqual(audit.select_event({'type': 'response_item', 'payload': payload}), payload)

    def test_incremental_source_and_partial_line(self):
        source = self.directory / 'source.jsonl'
        source.write_text(json.dumps({'timestamp': 't', 'type': 'response_item', 'payload': {'type': 'reasoning', 'text': 'private'}}) + '\n')
        state, lag = audit.sync_source(self.directory, source)
        self.assertEqual(state['lines'], 1)
        self.assertEqual(lag, 0)
        with source.open('a') as f:
            f.write('{"type":"event_msg"')
        state, lag = audit.sync_source(self.directory, source)
        self.assertEqual(state['lines'], 1)
        self.assertGreater(lag, 0)
        with source.open('a') as f:
            f.write(',"payload":{"type":"turn_aborted"}}\n')
        state, lag = audit.sync_source(self.directory, source)
        self.assertEqual(state['lines'], 2)
        self.assertEqual(audit.verify(self.directory)['events'], 2)
        self.assertNotIn('"text":"private"', (self.directory / 'events.jsonl').read_text())

    def test_replaced_or_truncated_source_stops(self):
        source = self.directory / 'source.jsonl'
        source.write_text('{"type":"event_msg","payload":{}}\n')
        audit.sync_source(self.directory, source)
        source.write_text('')
        with self.assertRaises(RuntimeError):
            audit.sync_source(self.directory, source)

    def test_full_source_verification_and_mutation(self):
        source = self.directory / 'source.jsonl'
        source.write_text('{"type":"event_msg","payload":{"type":"turn_aborted"}}\n')
        audit.atomic(self.directory / 'manifest.json', {'codex_source': str(source)})
        audit.sync_source(self.directory, source)
        proof = audit.verify_source(self.directory)
        self.assertEqual(proof['source_lines_verified'], 1)
        self.assertEqual(proof['source_bytes_verified'], source.stat().st_size)
        source.write_text(source.read_text().replace('turn_aborted', 'task_started'))
        with self.assertRaises(RuntimeError):
            audit.verify_source(self.directory)

    def test_artifact_checksum_verification(self):
        artifact = audit.preserve_bytes(self.directory, 'example.txt', b'original')
        audit.append_many(self.directory, [('external_artifact', artifact)])
        self.assertEqual(audit.verify(self.directory)['events'], 1)
        (self.directory / artifact['file']).write_bytes(b'changed')
        with self.assertRaises(RuntimeError):
            audit.verify(self.directory)

    def test_public_feed_only_has_allowed_projection(self):
        audit.publish('decision', 'Test <script> & test-secret-123 a@example.org')
        state = audit.public_state()
        self.assertFalse(state['audit']['healthy'])
        self.assertEqual(len(state['feed']), 1)
        self.assertNotIn('test-secret-123', json.dumps(state))
        self.assertNotIn('a@example.org', json.dumps(state))

    def test_send_refuses_without_recorder(self):
        with patch.object(session, 'alive', return_value=True), patch.object(session, 'tmux') as tmux:
            tmux.return_value.stdout = '0'
            with self.assertRaises(RuntimeError):
                session.send('6')
            self.assertFalse(any(call.args[0] == 'send-keys' for call in tmux.call_args_list))

    def test_input_intent_precedes_delivery(self):
        order = []
        with patch.object(session, 'alive', return_value=True), patch.object(session, 'screen', return_value='Dlvl:1 T:1'), \
             patch.object(audit, 'require_healthy'), patch.object(audit, 'publish'), \
             patch.object(audit, 'record', side_effect=lambda kind, data: order.append(kind)), \
             patch.object(session, 'tmux') as tmux:
            tmux.return_value.stdout = '0'
            tmux.side_effect = lambda *args, **kw: (order.append(args[0]) or type('R', (), {'stdout': '0'})())
            session.send('6')
        self.assertLess(order.index('input_requested'), order.index('send-keys'))
        self.assertLess(order.index('send-keys'), order.index('input_queued'))


if __name__ == '__main__':
    unittest.main()
