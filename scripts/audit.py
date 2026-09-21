#!/usr/bin/env python3
"""Private, hash-linked evidence ledger and an explicitly public spectator feed.

Local hashes detect changes relative to a trusted checkpoint; they are NOT an
independent timestamp or proof that the machine owner never supplied input.
"""
import argparse
import base64
from collections import Counter
from datetime import datetime, timezone
import fcntl
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import sys
import time
import uuid
from urllib.parse import urlparse, unquote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / '.runtime'
ZERO = '0' * 64
DISK_RESERVE = 5 * 1024 ** 3
MAX_SOURCE_LAG = 1024 ** 2


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def atomic(path, value):
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    fd = os.open(tmp, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, 'wb') as f:
        f.write(canonical(value) + b'\n'); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def active():
    config = json.loads((RUNTIME / 'audit-active.json').read_text())
    directory = Path(config['directory']).resolve()
    if directory.parent != (ROOT / 'records').resolve():
        raise RuntimeError('Audit directory must be directly inside records/.')
    return directory


@lru_cache(maxsize=1)
def secret_values():
    try:
        value = json.loads((RUNTIME / 'credentials.json').read_text()).get('password')
        return [value] if value else []
    except FileNotFoundError:
        return []


def clean(value, public=False):
    if isinstance(value, dict):
        return {k: '[REDACTED]' if re.fullmatch(r'(?i)(password|server_password|api_key|access_token|stream_key)', k)
                else clean(v, public) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v, public) for v in value]
    if isinstance(value, str):
        for secret in secret_values():
            value = value.replace(secret, '[REDACTED]')
        value = re.sub(r'\bsk-[A-Za-z0-9_-]{16,}', '[REDACTED API KEY]', value)
        if public:
            value = re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', '[email redacted]', value)
        return value
    return value


def tail(f):
    f.seek(0, os.SEEK_END)
    end = f.tell()
    if not end:
        return {'seq': 0, 'hash': ZERO}
    size = min(end, 8192)
    while True:
        f.seek(end - size)
        data = f.read(size)
        if not data.endswith(b'\n'):
            raise RuntimeError('Incomplete ledger tail: preserve and investigate before resuming.')
        lines = data.splitlines()
        if len(lines) > 1 or size == end:
            return json.loads(lines[-1])
        size = min(end, size * 2)


def append_many(directory, events):
    """One lock, append-only writes, fsync before acknowledging the batch."""
    path = directory / 'events.jsonl'
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_APPEND, 0o600)
    with os.fdopen(fd, 'a+b') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        previous = tail(f)
        f.seek(0, os.SEEK_END)
        for kind, data in events:
            row = {'seq': previous['seq'] + 1, 'recorded_at': now(),
                   'kind': kind, 'data': clean(data), 'previous_hash': previous['hash']}
            row['hash'] = hashlib.sha256(canonical(row)).hexdigest()
            f.write(canonical(row) + b'\n')
            previous = row
        f.flush(); os.fsync(f.fileno())
        return previous


def record(kind, data):
    return append_many(active(), [(kind, data)])


def verify(directory):
    previous = ZERO
    count = 0
    kinds = Counter()
    with (directory / 'events.jsonl').open('rb') as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        for count, line in enumerate(f, 1):
            row = json.loads(line)
            digest = row.pop('hash')
            if row['seq'] != count or row['previous_hash'] != previous or hashlib.sha256(canonical(row)).hexdigest() != digest:
                raise RuntimeError(f'Ledger integrity failure at row {count}.')
            kinds[row['kind']] += 1
            artifacts = ([row['data']] if row['kind'] == 'external_artifact' else
                         row['data'].get('artifacts', []) if row['kind'] == 'implementation_checkpoint' else [])
            for artifact in artifacts:
                path = (directory / artifact['file']).resolve()
                if not path.is_relative_to(directory.resolve()):
                    raise RuntimeError('Artifact path escapes evidence directory.')
                with path.open('rb') as saved:
                    if hashlib.file_digest(saved, 'sha256').hexdigest() != artifact['sha256']:
                        raise RuntimeError(f'Artifact checksum failure: {artifact["file"]}')
            previous = digest
    return {'events': count, 'head_sha256': previous, 'kinds': dict(kinds)}


def verify_source(directory, limit=None):
    source = Path(json.loads((directory / 'manifest.json').read_text())['codex_source'])
    expected_line = 1
    digest = hashlib.sha256()
    counts = Counter()
    unique_end = 0
    with source.open('rb') as original, (directory / 'events.jsonl').open('rb') as ledger:
        fcntl.flock(ledger, fcntl.LOCK_SH)
        for index, line in enumerate(ledger, 1):
            if limit is not None and index > limit:
                break
            row = json.loads(line)
            if row['kind'] != 'codex_record':
                continue
            q = row['data']
            if q['source_line'] > expected_line:
                raise RuntimeError(f'Transcript gap before source line {q["source_line"]}.')
            original.seek(q['source_offset'])
            raw = original.readline()
            if hashlib.sha256(raw).hexdigest() != q['source_sha256']:
                raise RuntimeError(f'Transcript source changed at line {q["source_line"]}.')
            if clean(select_event(json.loads(raw))) != q['content']:
                raise RuntimeError(f'Transcript projection mismatch at line {q["source_line"]}.')
            if q['source_line'] == expected_line:
                if q['source_offset'] != unique_end or original.tell() != q['source_end']:
                    raise RuntimeError('Transcript byte coverage gap.')
                unique_end = original.tell()
                digest.update(raw)
                expected_line += 1
                content = q['content']
                counts[content.get('type', q['source_type']) if content else 'explicitly_omitted'] += 1
    return {'source_lines_verified': expected_line - 1, 'source_bytes_verified': unique_end,
            'source_prefix_sha256': digest.hexdigest(), 'source_counts': dict(counts)}


def preserve_bytes(directory, name, data):
    digest = hashlib.sha256(data).hexdigest()
    target = directory / 'artifacts' / (digest + '-' + Path(name).name)
    target.parent.mkdir(mode=0o700, exist_ok=True)
    try:
        fd = os.open(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise RuntimeError('Previously saved artifact changed.')
    else:
        with os.fdopen(fd, 'wb') as f:
            f.write(data); f.flush(); os.fsync(f.fileno())
    return {'file': str(target.relative_to(directory)), 'sha256': digest, 'bytes': len(data)}


def publish(kind, text, **details):
    # This file contains ONLY intentionally public commentary and game inputs.
    path = RUNTIME / 'public-feed.json'
    lock_fd = os.open(RUNTIME / 'public-feed.lock', os.O_CREAT | os.O_RDWR, 0o600)
    with os.fdopen(lock_fd, 'w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            rows = json.loads(path.read_text())
        except FileNotFoundError:
            rows = []
        rows.append(clean({'id': uuid.uuid4().hex, 'at': now(), 'kind': kind,
                           'text': text, **details}, public=True))
        atomic(path, rows[-80:])


def public_state():
    try:
        feed = json.loads((RUNTIME / 'public-feed.json').read_text())
    except FileNotFoundError:
        feed = []
    try:
        health = json.loads((RUNTIME / 'audit-health.json').read_text())
        health['healthy'] = (time.time() - health.get('epoch', 0) < 15 and not health.get('error')
                             and health.get('terminal_pipe', False)
                             and health.get('free_bytes', 0) >= DISK_RESERVE
                             and health.get('source_lag_bytes', MAX_SOURCE_LAG + 1) <= MAX_SOURCE_LAG)
        # Never expose local paths, raw transcript, or exception details.
        health = {k: health.get(k) for k in ('healthy', 'updated_at', 'source_lines', 'source_lag_bytes', 'head_sha256', 'free_bytes')}
    except FileNotFoundError:
        health = {'healthy': False}
    return {'feed': feed, 'audit': health}


def require_healthy():
    if not public_state()['audit']['healthy']:
        raise RuntimeError('Audit recorder is not healthy. Restart scripts/audit.py watch before sending game input.')
    config = json.loads((active() / 'manifest.json').read_text())
    thread = os.environ.get('CODEX_THREAD_ID') or os.environ.get('CODEX_SESSION_ID')
    if thread and thread != config['thread_id']:
        raise RuntimeError('Recorder is bound to a different Codex thread. Register this session before input.')
    if shutil.disk_usage(ROOT).free < DISK_RESERVE:
        raise RuntimeError('Disk reserve reached: game input paused below 5 GiB free.')
    health = json.loads((RUNTIME / 'audit-health.json').read_text())
    source = Path(config['codex_source'])
    if source.stat().st_size - health.get('source_offset', 0) > MAX_SOURCE_LAG:
        raise RuntimeError('Transcript recorder is more than 1 MiB behind. Wait for it to catch up.')


def select_event(event):
    """Export observable messages/actions, never private reasoning/instructions."""
    kind = event.get('type')
    q = event.get('payload', {})
    typ = q.get('type')
    if kind == 'session_meta':
        return {k: q[k] for k in ('id', 'timestamp', 'cwd', 'originator', 'cli_version', 'model_provider') if k in q}
    if kind == 'turn_context':
        return {k: q[k] for k in ('turn_id', 'root_turn_id', 'cwd', 'model', 'effort', 'current_date', 'timezone') if k in q}
    if kind == 'response_item':
        if typ == 'message' and (q.get('role') == 'user' or
                q.get('role') == 'assistant' and q.get('phase') in ('commentary', 'final_answer')):
            return {k: q[k] for k in ('type', 'id', 'role', 'phase', 'content') if k in q}
        if typ in ('function_call', 'function_call_output', 'custom_tool_call', 'custom_tool_call_output'):
            return {k: q[k] for k in ('type', 'id', 'call_id', 'name', 'input', 'arguments', 'output', 'status') if k in q}
    if kind == 'event_msg' and typ in ('task_started', 'task_complete', 'turn_aborted'):
        return {k: q[k] for k in ('type', 'turn_id', 'started_at', 'completed_at', 'duration_ms') if k in q}
    return None


def sync_source(directory, source, live=False):
    fd = os.open(directory / 'source.lock', os.O_CREAT | os.O_RDWR, 0o600)
    with os.fdopen(fd, 'w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _sync_source(directory, source, live)


def _sync_source(directory, source, live=False):
    cursor_path = directory / 'source-cursor.json'
    try:
        state = json.loads(cursor_path.read_text())
    except FileNotFoundError:
        state = {'offset': 0, 'lines': 0, 'turn_id': None}
    stat = source.stat()
    identity = [stat.st_dev, stat.st_ino]
    if state.get('identity', identity) != identity or stat.st_size < state['offset']:
        raise RuntimeError('Transcript source replaced or truncated; refusing to silently skip evidence.')
    state['identity'] = identity
    batch = []
    public = []
    with source.open('rb') as f:
        f.seek(state['offset'])
        for _ in range(1000):
            start = f.tell()
            line = f.readline()
            if not line.endswith(b'\n'):
                break  # active writer may not have finished this JSON record yet
            event = json.loads(line)
            q = event.get('payload', {})
            if event.get('type') == 'turn_context' or q.get('type') == 'task_started':
                state['turn_id'] = q.get('turn_id', state['turn_id'])
            selected = select_event(event)
            state['lines'] += 1
            state['offset'] = f.tell()
            batch.append(('codex_record', {
                'source_line': state['lines'], 'source_offset': start,
                'source_end': state['offset'], 'source_sha256': hashlib.sha256(line).hexdigest(),
                'source_timestamp': event.get('timestamp'), 'turn_id': state['turn_id'],
                'source_type': event.get('type'), 'payload_type': q.get('type'),
                'content': selected, 'omitted': None if selected is not None else 'private_or_duplicate_metadata'}))
            if live and selected and selected.get('role') == 'assistant' and selected.get('phase') == 'commentary':
                text = '\n'.join(c.get('text', '') for c in selected.get('content', []) if c.get('type') in ('text', 'output_text'))
                if text:
                    public.append(text)
    if batch:
        append_many(directory, batch)
        # A crash between fsync and this cursor update can duplicate a source
        # range, never lose it. Source line/offset make duplicates explicit.
        atomic(cursor_path, state)
        if (RUNTIME / 'broadcast.enabled').exists():
            for text in public:
                publish('decision', text, source='assistant commentary')
    return state, max(0, source.stat().st_size - state['offset'])


def watch(directory):
    import session
    config = json.loads((directory / 'manifest.json').read_text())
    source = Path(config['codex_source'])
    lock = os.fdopen(os.open(directory / 'watch.lock', os.O_CREAT | os.O_RDWR, 0o600), 'w')
    os.fchmod(lock.fileno(), 0o600)
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    previous_screen = None
    while True:
        state, lag = sync_source(directory, source, live=True)
        if not lag:
            visible = (RUNTIME / 'broadcast.enabled').exists()
            current = session.screen(ansi=True) if visible else '[capture hidden for privacy]'
            if current != previous_screen:
                append_many(directory, [('terminal_snapshot', {'ansi': current, 'cols': session.COLS, 'rows': session.ROWS})])
                previous_screen = current
        with (directory / 'events.jsonl').open('rb') as f:
            fcntl.flock(f, fcntl.LOCK_SH)
            head = tail(f)
        atomic(RUNTIME / 'audit-health.json', {'epoch': time.time(), 'updated_at': now(),
            'source_lines': state['lines'], 'source_lag_bytes': lag, 'head_sha256': head['hash'],
            'source_offset': state['offset'], 'free_bytes': shutil.disk_usage(ROOT).free,
            'terminal_pipe': session.tmux('display-message', '-p', '-t', session.TARGET, '#{pane_pipe}').stdout.strip() == '1'})
        time.sleep(0.05 if lag else 1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    init = sub.add_parser('init')
    init.add_argument('--source', type=Path, required=True)
    init.add_argument('--label', default='NetHack evidence')
    for name in ('start', 'sync', 'watch', 'verify', 'status', 'tty', 'checkpoint'):
        sub.add_parser(name)
    fetch = sub.add_parser('fetch', help='Preserve an explicitly selected public evidence URL, up to 64 MiB')
    fetch.add_argument('url')
    args = p.parse_args()
    RUNTIME.mkdir(mode=0o700, exist_ok=True)
    if args.command == 'init':
        if (RUNTIME / 'audit-active.json').exists():
            raise RuntimeError('An audit ledger is already configured; do not silently replace it.')
        with args.source.open('rb') as f:
            meta = json.loads(f.readline()).get('payload', {})
        if meta.get('cwd') != str(ROOT):
            raise RuntimeError('Source transcript belongs to a different workspace.')
        directory = ROOT / 'records' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
        directory.mkdir(parents=True, mode=0o700)
        os.chmod(directory.parent, 0o700)
        manifest = {'schema': 1, 'label': args.label, 'created_at': now(),
                    'codex_source': str(args.source.resolve()), 'thread_id': meta.get('id'),
                    'retroactive_import': True, 'terminal_capture_from': now(),
                    'exclusions': ['private reasoning', 'system/developer instructions', 'duplicate internal events', 'known credentials'],
                    'limits': ['No independent timestamp anchor yet', 'No proof against out-of-band terminal input',
                               'Earlier tool outputs may be truncated by the original tools', 'No retroactive raw terminal capture']}
        atomic(directory / 'manifest.json', manifest)
        append_many(directory, [('audit_started', manifest)])
        atomic(RUNTIME / 'audit-active.json', {'directory': str(directory)})
        print(directory)
        return
    directory = active()
    if args.command == 'start':
        import session
        script = str(Path(__file__).resolve())
        if session.tmux('display-message', '-p', '-t', session.TARGET, '#{pane_pipe}').stdout.strip() == '0':
            session.tmux('pipe-pane', '-o', '-t', session.TARGET, shlex.join([sys.executable, script, 'tty']))
        if session.tmux('has-session', '-t', 'audit', check=False).returncode:
            session.tmux('new-session', '-d', '-s', 'audit', sys.executable, script, 'watch')
        elif session.tmux('display-message', '-p', '-t', 'audit:0.0', '#{pane_dead}').stdout.strip() == '1':
            session.tmux('respawn-pane', '-t', 'audit:0.0', sys.executable, script, 'watch')
        print('Recorder started or already running. Check audit.py status before gameplay.')
    elif args.command == 'sync':
        source = Path(json.loads((directory / 'manifest.json').read_text())['codex_source'])
        previous_offset = -1
        while True:
            state, lag = sync_source(directory, source)
            if not lag or state['offset'] == previous_offset:
                break
            previous_offset = state['offset']
        print(json.dumps({'source_lines': state['lines'], 'source_bytes': state['offset']}))
    elif args.command == 'verify':
        proof = verify(directory)
        print(json.dumps({**proof, **verify_source(directory, proof['events'])}))
    elif args.command == 'status':
        print(json.dumps({'directory': str(directory), **public_state()['audit']}))
    elif args.command == 'checkpoint':
        paths = [ROOT / 'README.md', ROOT / 'EVIDENCE.md', ROOT / 'AGENTS.md', ROOT / 'web/index.html', ROOT / 'config/nethackrc']
        paths += list((ROOT / 'scripts').glob('*.py')) + list((ROOT / 'scripts').glob('*.mjs')) + list((ROOT / 'memory').glob('*.md')) + list((ROOT / 'memory').glob('*.json'))
        artifacts = [dict(preserve_bytes(directory, p.name, p.read_bytes()), source=str(p.relative_to(ROOT))) for p in paths if p.exists()]
        append_many(directory, [('implementation_checkpoint', {'artifacts': artifacts})])
        proof = verify(directory)
        checkpoint = {'created_at': now(), **proof, **verify_source(directory, proof['events'])}
        path = directory / ('checkpoint-' + uuid.uuid4().hex + '.json')
        atomic(path, checkpoint)
        print(json.dumps({'file': str(path), **checkpoint}))
    elif args.command == 'fetch':
        url = urlparse(args.url)
        if url.scheme != 'https' or not url.hostname or url.username or url.password:
            raise RuntimeError('Evidence downloads require a public HTTPS URL without credentials.')
        with urlopen(Request(args.url, headers={'User-Agent': 'CodexDelver-Evidence/1.0'}), timeout=20) as response:
            data = response.read(64 * 1024 * 1024 + 1)
            if len(data) > 64 * 1024 * 1024:
                raise RuntimeError('Evidence file exceeds the 64 MiB safety limit.')
            artifact = preserve_bytes(directory, unquote(url.path.rsplit('/', 1)[-1]) or 'index.html', data)
            artifact.update({'source_url': args.url, 'resolved_url': response.url,
                             'retrieved_at': now(), 'etag': response.headers.get('ETag'),
                             'last_modified': response.headers.get('Last-Modified')})
        append_many(directory, [('external_artifact', artifact)])
        print(json.dumps(artifact))
    elif args.command == 'watch':
        try:
            watch(directory)
        except Exception:
            atomic(RUNTIME / 'audit-health.json', {'epoch': time.time(), 'updated_at': now(), 'error': 'recorder stopped'})
            raise
    elif args.command == 'tty':
        append_many(directory, [('terminal_pipe_started', {'pid': os.getpid()})])
        while True:
            data = os.read(sys.stdin.fileno(), 65536)
            if not data:
                break
            visible = (RUNTIME / 'broadcast.enabled').exists()
            append_many(directory, [('terminal_output', {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                'base64': base64.b64encode(data).decode() if visible else None, 'hidden': not visible})])
        append_many(directory, [('terminal_pipe_closed', {})])


if __name__ == '__main__':
    main()
