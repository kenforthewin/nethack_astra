#!/usr/bin/env python3
"""Verify a public export without needing the private ledger or any credentials."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def verify(directory):
    directory = directory.resolve()
    expected = set()
    for line in (directory / 'SHA256SUMS').read_text().splitlines():
        checksum, relative = line.split('  ', 1)
        path = directory / relative
        if path.is_symlink() or not path.resolve().is_relative_to(directory):
            raise ValueError('unsafe path')
        if relative in expected:
            raise ValueError('duplicate checksum entry')
        expected.add(relative)
        with path.open('rb') as f:
            actual = hashlib.file_digest(f, 'sha256').hexdigest()
        if actual != checksum:
            raise ValueError('checksum mismatch: ' + relative)
    actual_files = {str(p.relative_to(directory)) for p in directory.rglob('*') if p.is_file()
                    and '.git' not in p.relative_to(directory).parts
                    and '__pycache__' not in p.relative_to(directory).parts
                    and p.name != 'SHA256SUMS'}
    if actual_files != expected:
        raise ValueError('unlisted or missing files: ' + repr(sorted(actual_files ^ expected)))
    count = 0
    if (directory / 'events.jsonl.gz').exists():
        manifest = json.loads((directory / 'manifest.json').read_text())
        previous = '0' * 64
        with gzip.open(directory / 'events.jsonl.gz', 'rt') as f:
            for count, line in enumerate(f, 1):
                row = json.loads(line); recorded = row.pop('hash')
                if row['source_seq'] != count or row['previous_hash'] != previous:
                    raise ValueError('sequence or chain discontinuity at ' + str(count))
                if hashlib.sha256(canonical(row)).hexdigest() != recorded:
                    raise ValueError('event hash mismatch at ' + str(count))
                previous = recorded
        if count != manifest['exported_event_count'] or previous != manifest['exported_head_sha256']:
            raise ValueError('manifest does not match public event chain')
    return {'files_verified': len(expected), 'events_verified': count}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', type=Path)
    print(json.dumps(verify(p.parse_args().directory)))
