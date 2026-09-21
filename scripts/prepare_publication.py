#!/usr/bin/env python3
"""Build a conservative, offline public evidence projection. Never upload.

Original archives are read-only. A new destination is required on each build.
Unknown event types and arbitrary tool bodies are withheld, not guessed safe.
"""
import argparse
import base64
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re
import struct
import tarfile
from urllib.parse import quote, urlparse

import audit

ROOT = Path(__file__).resolve().parents[1]
ANSI = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]|\x1b\][^\x07]*(?:\x07|\x1b\\)')
SECRET_KEY = re.compile(r'(?i)^(?:password|server_password|api_key|access_token|refresh_token|stream_key|key|token)$')
PATTERNS = {
    'email': re.compile(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}'),
    'home_path': re.compile(r'/(?:Users|home)/[^/\s\"\'<>]+'),
    'lan_address': re.compile(r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b'),
    'api_token': re.compile(r'\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b'),
    'bearer_token': re.compile(r'(?i)Bearer\s+[A-Za-z0-9._~+/=-]{12,}'),
    'private_key': re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----', re.S),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def known_secrets(root):
    """Only read in-scope credential stores; never print values or their hashes."""
    files = [root / '.runtime/credentials.json']
    obs = Path.home() / 'Library/Application Support/obs-studio'
    files += [obs / 'plugin_config/obs-websocket/config.json']
    files += list((obs / 'basic/profiles').glob('*/service.json'))
    result = set()

    def visit(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if SECRET_KEY.fullmatch(k) and isinstance(v, str) and len(v) >= 6:
                    result.update((v, quote(v, safe=''), json.dumps(v)[1:-1],
                                   base64.b64encode(v.encode()).decode()))
                else:
                    visit(v)
        elif isinstance(value, list):
            for v in value:
                visit(v)
    for path in files:
        if path.exists():
            visit(json.loads(path.read_text()))
    return sorted(result, key=len, reverse=True)


# Reviewed public endpoints and synthetic fixtures: source-code exceptions only.
PUBLIC_CODE_LITERALS = frozenset((
    'nethack@us.hardfought.org', 'nethack@hardfought.org',
    'a+b@example.org', 'a@example.org', 'test+run@example.org',
    '/Users/alice', '192.168.1.25',
))


class Redactor:
    def __init__(self, secrets=(), allowed=()):
        self.secrets = secrets
        self.allowed = frozenset(allowed)
        self.counts = Counter()

    def text(self, value):
        for secret in self.secrets:
            n = value.count(secret)
            if n:
                self.counts['known_secret'] += n
                value = value.replace(secret, '[REDACTED:credential]')
        for name, pattern in PATTERNS.items():
            def replace(match):
                if match.group() in self.allowed:
                    return match.group()
                self.counts[name] += 1
                return '[REDACTED:' + name + ']'
            value = pattern.sub(replace, value)
        return value

    def clean(self, value):
        if isinstance(value, str):
            return self.text(value)
        if isinstance(value, list):
            return [self.clean(v) for v in value]
        if isinstance(value, dict):
            return {k: self.clean(v) for k, v in value.items()}
        return value

    def findings(self, text):
        probe = Redactor(self.secrets, self.allowed)
        probe.text(text)
        probe.text(ANSI.sub('', text))
        return {k: n for k, n in probe.counts.items() if n}


FIELDS = {
    'public_decision': ('text',),
    'terminal_snapshot': ('ansi', 'cols', 'rows'),
    'agent_observation': ('screen', 'compact_display'),
    'input_requested': ('command_id', 'input', 'named', 'sensitive', 'screen_before', 'game_turn', 'source'),
    'input_queued': ('command_id',), 'input_failed': ('command_id',),
    'guarded_step': ('key', 'screen_after', 'stop'),
    'guarded_batch': ('requested', 'sent_steps', 'stop'),
    'sokoban_plan': ('allow_pet_swaps', 'boulder', 'initial_boulders', 'initial_hero', 'initial_highlighted_pets', 'initial_holes', 'inspect_bystanders', 'keys', 'max_steps', 'pushes'),
    'sokoban_step': ('expected_boulders', 'expected_hero', 'expected_holes', 'key', 'screen_after'),
    'sokoban_attitude_check': ('confirmed_peaceful', 'glyph', 'position', 'screen_after'),
    'input_preflight_rejected': ('cursor', 'input', 'reason', 'screen'),
    'raw_input_override': ('input', 'reason'),
    'stash_gold_step': ('input', 'observation'),
    'run_preparation': ('alignment', 'cutoff', 'gender', 'local_video', 'race', 'role', 'run_id', 'storage', 'user_authorized', 'vod_enabled'),
}


def project(row, redactor):
    kind, data = row['kind'], row['data']
    result = {'source_seq': row['seq'], 'recorded_at': row['recorded_at'], 'kind': kind}
    if kind in FIELDS:
        safe = {k: data[k] for k in FIELDS[kind] if k in data}
        if kind == 'input_requested' and data.get('sensitive'):
            safe['input'] = None
            safe['screen_before'] = '[withheld: sensitive input]'
        result['data'] = redactor.clean(safe)
    elif kind == 'codex_record':
        result['source_line'] = data['source_line']
        result['source_timestamp'] = data.get('source_timestamp')
        c = data.get('content') or {}
        typ = c.get('type')
        if typ == 'message' and (c.get('role') == 'user' or
                c.get('role') == 'assistant' and c.get('phase') in ('commentary', 'final_answer')):
            text = '\n'.join(x.get('text', '') for x in c.get('content', [])
                             if x.get('type') in ('text', 'input_text', 'output_text'))
            if c.get('role') == 'user' and (text.lstrip().startswith('<environment_context>') or
                                          text.lstrip().startswith('# AGENTS.md instructions')):
                result['omitted'] = 'injected workspace instructions/environment; see published journals and harness'
            else:
                result['data'] = {'role': c['role'], 'phase': c.get('phase'), 'text': redactor.text(text)}
        elif data.get('source_type') == 'turn_context':
            result['data'] = {k: c[k] for k in ('turn_id', 'model', 'effort', 'current_date') if k in c}
        elif typ in ('task_started', 'task_complete', 'turn_aborted'):
            result['data'] = {k: c[k] for k in ('type', 'turn_id', 'started_at', 'completed_at', 'duration_ms') if k in c}
        elif typ in ('custom_tool_call', 'function_call', 'custom_tool_call_output', 'function_call_output'):
            result['data'] = {k: c[k] for k in ('type', 'name', 'call_id', 'status') if k in c}
            result['omitted'] = 'arbitrary tool body withheld; game commands/observations exported separately'
        else:
            result['omitted'] = 'private reasoning, instructions, duplicate/internal metadata or unselected source record'
    elif kind == 'terminal_output':
        result['data'] = {k: data[k] for k in ('bytes', 'hidden') if k in data}
        result['omitted'] = 'raw terminal byte chunks withheld; use reviewed snapshots and server ttyrecs'
    elif kind == 'implementation_checkpoint':
        result['data'] = {'artifacts': [redactor.clean({k: a[k] for k in ('file', 'sha256', 'bytes', 'source') if k in a})
                                        for a in data['artifacts']]}
        result['note'] = 'original hashes; consult artifact-index for exported derived hashes or omissions'
    elif kind == 'external_artifact':
        result['data'] = redactor.clean({k: data[k] for k in ('file', 'sha256', 'bytes', 'source_url', 'retrieved_at', 'last_modified') if k in data})
    else:
        result['omitted'] = 'event metadata not on public allowlist'
    return result


def tty_payload(raw):
    """Validate standard little-endian ttyrec and join frames for cross-frame scanning."""
    offset = 0
    frames = []
    times = []
    while offset < len(raw):
        if len(raw) - offset < 12:
            raise ValueError('incomplete ttyrec header')
        sec, usec, size = struct.unpack_from('<III', raw, offset)
        offset += 12
        if usec >= 1_000_000 or size > len(raw) - offset:
            raise ValueError('invalid/incomplete ttyrec frame')
        frames.append(raw[offset:offset + size]); times.append(sec + usec / 1e6)
        offset += size
    if not frames:
        raise ValueError('empty ttyrec')
    return b''.join(frames).decode('utf-8', errors='replace'), {
        'frames': len(frames), 'first_epoch': times[0], 'last_epoch': times[-1],
        'chronological': all(a <= b for a, b in zip(times, times[1:]))}


def safe_file(base, relative):
    p = base / relative
    if p.is_symlink() or not p.resolve().is_relative_to(base.resolve()):
        raise ValueError('unsafe artifact path')
    return p


def export_artifacts(source, target, rows, redactor):
    """Export historical code/docs and one latest recording per server segment.

    Third-party source is indexed by URL, not redistributed. Binary records
    must pass scanning unchanged; otherwise withhold rather than corrupt them.
    """
    latest = {}
    for row in rows:
        if row['kind'] == 'external_artifact':
            a = row['data']; url = a.get('source_url', '')
            if '/ttyrec/' in url:
                name = url.rsplit('/', 1)[-1].removesuffix('.gz')
                previous = latest.get(name)
                if previous is None or (url.endswith('.gz'), a.get('retrieved_at', '')) > (
                        previous.get('source_url', '').endswith('.gz'), previous.get('retrieved_at', '')):
                    latest[name] = a
    selected = {a['file'] for a in latest.values()}
    artifacts = {}
    for row in rows:
        entries = row['data'].get('artifacts', []) if row['kind'] == 'implementation_checkpoint' else [row['data']]
        for a in entries:
            if a['file'] in artifacts:
                continue
            entry = {k: redactor.clean(a[k]) for k in ('file', 'source', 'source_url', 'sha256', 'bytes', 'retrieved_at') if k in a}
            artifacts[a['file']] = entry
            original = safe_file(source, a['file']).read_bytes()
            if digest(original) != a['sha256']:
                raise ValueError('artifact checksum mismatch')
            url = a.get('source_url', '')
            parsed = urlparse(url)
            recording = '/ttyrec/' in parsed.path and parsed.path.endswith(('.ttyrec', '.ttyrec.gz'))
            public_server = parsed.hostname in ('www.hardfought.org', 'hdf-us.s3.amazonaws.com')
            code = row['kind'] == 'implementation_checkpoint' and (
                a.get('source', '').startswith(('scripts/', 'memory/', 'web/', 'config/')) or
                a.get('source') in ('README.md', 'EVIDENCE.md', 'AGENTS.md'))
            dump_text = public_server and '/dumplog/' in parsed.path and parsed.path.endswith('.txt')
            if recording and public_server and a['file'] in selected:
                try:
                    text, timing = tty_payload(gzip.decompress(original) if url.endswith('.gz') else original)
                    findings = redactor.findings(text)
                    if findings:
                        entry['omitted'] = 'recording failed privacy scan'
                        entry['finding_categories'] = findings
                        continue
                    entry['ttyrec'] = timing
                    entry['coverage'] = 'final compressed server segment' if url.endswith('.gz') else 'partial snapshot; finalization not established'
                    output = original
                except (ValueError, EOFError, OSError) as exc:
                    entry['omitted'] = 'invalid or incomplete ttyrec: ' + type(exc).__name__
                    continue
            elif code or dump_text:
                cleaner = Redactor(redactor.secrets, PUBLIC_CODE_LITERALS) if (
                    code and a.get('source', '').endswith(('.py', '.mjs'))) else redactor
                output = cleaner.text(original.decode('utf-8')).encode()
                if cleaner is not redactor:
                    redactor.counts.update(cleaner.counts)
                if cleaner.findings(output.decode()):
                    entry['omitted'] = 'text failed normalized privacy scan'
                    continue
            else:
                entry['omitted'] = ('superseded recording snapshot' if recording else
                                    'third-party source or HTML/directory listing: retain URL, not body')
                continue
            relative = 'artifacts/' + Path(a['file']).name
            destination = target / relative
            destination.parent.mkdir(exist_ok=True, parents=True)
            destination.write_bytes(output)
            entry.update(exported_file=relative, exported_sha256=digest(output), exported_bytes=len(output),
                         transformed=output != original)
    return list(artifacts.values())


def export(source, checkpoint, destination, secrets):
    # Refuse reuse, including pre-existing empty destinations and symlinks.
    destination.mkdir(parents=True, exist_ok=False)
    destination.chmod(0o700)
    repo = destination / 'repo'; repo.mkdir()
    evidence = destination / 'evidence'; evidence.mkdir()
    private = destination / 'private-review'; private.mkdir(mode=0o700)
    redactor = Redactor(secrets)
    cutoff = json.loads(checkpoint.read_text())
    previous = audit.ZERO
    source_hash = hashlib.sha256()
    counts, omitted, models = Counter(), Counter(), Counter()
    artifact_rows, users, changes = [], [], []
    exported_head = audit.ZERO
    with (source / 'events.jsonl').open('rb') as stream, gzip.open(evidence / 'events.jsonl.gz', 'wt') as out:
        for index in range(1, cutoff['events'] + 1):
            raw = stream.readline(); row = json.loads(raw)
            original_hash = row.pop('hash')
            if row['seq'] != index or row['previous_hash'] != previous or digest(audit.canonical(row)) != original_hash:
                raise ValueError('original ledger validation failed at ' + str(index))
            previous = original_hash; source_hash.update(raw)
            before = redactor.counts.copy()
            projected = project(row, redactor)
            # Decode escape sequences in the actual strings, not serialized JSON,
            # for a second check against ANSI-obscured sensitive text.
            def check(value):
                if isinstance(value, str):
                    return redactor.findings(value)
                if isinstance(value, dict):
                    return any(check(v) for v in value.values())
                if isinstance(value, list):
                    return any(check(v) for v in value)
                return False
            if check(projected):
                projected.pop('data', None)
                projected['omitted'] = 'content withheld: normalized privacy scan'
            if projected.get('omitted'):
                omitted[projected['omitted']] += 1
            delta = redactor.counts - before
            if delta:
                changes.append({'source_seq': index, 'categories': dict(delta)})
            if row['kind'] in ('external_artifact', 'implementation_checkpoint'):
                artifact_rows.append(row)
            d = projected.get('data', {})
            if d.get('role') == 'user':
                users.append(projected.copy())
            if d.get('model'):
                models[(d['model'], str(d.get('effort')))] += 1
            counts[row['kind']] += 1
            projected['previous_hash'] = exported_head
            exported_head = digest(audit.canonical(projected))
            projected['hash'] = exported_head
            out.write(audit.canonical(projected).decode() + '\n')
    if previous != cutoff['head_sha256']:
        raise ValueError('checkpoint head does not match ledger prefix')
    print('Ledger projection complete; exporting reviewed artifacts.', flush=True)
    artifact_index = export_artifacts(source, evidence, artifact_rows, redactor)
    dump(evidence / 'artifact-index.json', artifact_index)
    dump(evidence / 'human-messages.json', users)
    dump(evidence / 'redactions.json', {'policy': 'docs/PUBLICATION.md', 'event_redactions': changes,
                                      'omission_counts': omitted, 'replacement_counts': redactor.counts})
    # Exact allowlist, not a recursive workspace copy.
    paths = list((ROOT / 'scripts').glob('*.py')) + list((ROOT / 'scripts').glob('*.mjs'))
    paths += [ROOT / p for p in ('config/tmux.conf', 'config/nethackrc', 'config/known_hosts',
                                'web/index.html', 'web/game.html', 'EVIDENCE.md')]
    paths += list((ROOT / 'memory').glob('*.md')) + list((ROOT / 'memory').glob('*.json'))
    paths += list((ROOT / 'publication-src').rglob('*'))
    file_index = []
    for p in sorted(paths):
        if not p.is_file() or p.is_symlink():
            continue
        relative = p.relative_to(ROOT)
        if relative.parts[0] == 'publication-src':
            relative = relative.relative_to('publication-src')
        cleaner = Redactor(redactor.secrets, PUBLIC_CODE_LITERALS) if p.suffix in ('.py', '.mjs') else redactor
        data = p.read_bytes(); clean = cleaner.text(data.decode()).encode()
        if cleaner is not redactor:
            redactor.counts.update(cleaner.counts)
        if cleaner.findings(clean.decode()):
            raise ValueError('source file failed privacy scan: ' + str(relative))
        target = repo / relative; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(clean)
        file_index.append({'file': str(relative), 'original_sha256': digest(data),
                           'exported_sha256': digest(clean), 'transformed': data != clean})
    dump(repo / 'docs/source-export.json', file_index)
    recording_lines = ['# Server recording inventory', '',
        'Selected retained segments, not a claim of uninterrupted coverage. Times are UTC.', '',
        '| Segment | First frame | Last frame | Retained copy |',
        '| --- | --- | --- | --- |']
    for a in artifact_index:
        if 'ttyrec' in a:
            start = datetime.fromtimestamp(a['ttyrec']['first_epoch'], timezone.utc).isoformat()
            end = datetime.fromtimestamp(a['ttyrec']['last_epoch'], timezone.utc).isoformat()
            recording_lines.append('| [' + a['source_url'].rsplit('/', 1)[-1] + '](' + a['source_url'] + ') | '
                                   + start + ' | ' + end + ' | ' + a['coverage'] + ' |')
    (repo / 'docs/RECORDINGS.md').write_text('\n'.join(recording_lines) + '\n')
    manifest = {
        'schema': 1, 'created_at': datetime.now(timezone.utc).isoformat(),
        'status': 'local release candidate; not uploaded; license choice and owner review pending',
        'checkpoint': cutoff, 'original_ledger_prefix_sha256': source_hash.hexdigest(),
        'exported_event_count': cutoff['events'], 'exported_head_sha256': exported_head,
        'event_kinds': counts, 'omission_counts': omitted,
        'model_context_counts': [{'model': m, 'effort': e, 'contexts': n} for (m, e), n in sorted(models.items())],
        'scope': 'Whole recorded campaign prefix, including failed runs; not just the winning run.',
        'limits': ['Filtered projection, not complete raw transcript.',
                   'Arbitrary tool bodies withheld; all original sequence numbers retained as records or omission markers.',
                   'No retroactive terminal capture before recorder activation.',
                   'Original source prefix checked privately; public cannot recheck withheld raw source.',
                   'Hashes are not independent timestamps or proof against owner alteration or out-of-band input.',
                   'Recording segment inventory does not establish uninterrupted coverage.',
                   'No Twitch VOD archive included; no absence-of-human-help claim.',
                   'Automated privacy scanning and selective manual review cannot guarantee absence of all personal data.'],
    }
    dump(evidence / 'manifest.json', manifest)
    dump(repo / 'docs/evidence-manifest.json', manifest)
    dump(private / 'review-summary.json', {'replacements': redactor.counts, 'omissions': omitted,
        'files_reviewed_by_policy': len(file_index), 'artifacts_indexed': len(artifact_index),
        'artifacts_exported': sum('exported_file' in a for a in artifact_index),
        'human_messages': len(users), 'manual_review': 'See docs/PUBLICATION.md; no blanket certification.'})
    for target in (repo, evidence):
        checksums = []
        for p in sorted(target.rglob('*')):
            if p.is_file():
                checksums.append(digest(p.read_bytes()) + '  ' + str(p.relative_to(target)))
        (target / 'SHA256SUMS').write_text('\n'.join(checksums) + '\n')
    archive = destination / 'nethack-evidence.tar.gz'
    with tarfile.open(archive, 'w:gz') as tar:
        def scrub(info):
            info.uid = info.gid = 0; info.uname = info.gname = ''
            info.mode = 0o755 if info.isdir() else 0o644
            return info
        tar.add(evidence, arcname='evidence', filter=scrub)
    sha = digest(archive.read_bytes())
    (destination / 'SHA256SUMS').write_text(sha + '  ' + archive.name + '\n')
    print(json.dumps({'destination': str(destination), 'archive_bytes': archive.stat().st_size,
                      'archive_sha256': sha, 'events': cutoff['events'], 'omissions': omitted,
                      'artifacts_exported': sum('exported_file' in a for a in artifact_index)}))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--records', type=Path, required=True)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--destination', type=Path, required=True)
    args = p.parse_args()
    source = args.records.resolve()
    destination = args.destination.resolve()
    if destination.is_relative_to(source) or destination == ROOT or source.is_relative_to(destination):
        raise SystemExit('Destination must be separate from original evidence and workspace root.')
    export(source, args.checkpoint, destination, known_secrets(ROOT))


if __name__ == '__main__':
    main()
