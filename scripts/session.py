#!/usr/bin/env python3
"""Persistent Hardfought terminal and a read-only broadcast view; stdlib only."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import secrets
import subprocess
import sys
import time
import uuid
import audit
import guard
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from terminal import text_runs

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / '.runtime'
SOCKET = '/tmp/nhstream-' + hashlib.sha256(str(ROOT).encode()).hexdigest()[:12] + '.sock'
TARGET = 'hardfought:0.0'
COLS, ROWS = 144, 36


def tmux(*args, check=True):
    return subprocess.run(['tmux', '-S', SOCKET, *args], text=True,
                          capture_output=True, check=check)


def alive():
    return tmux('has-session', '-t', 'hardfought', check=False).returncode == 0


def screen(ansi=False):
    if not alive():
        return 'No Hardfought terminal connected.'
    captured = tmux('capture-pane', '-p', '-e', '-t', TARGET).stdout
    return captured if ansi else ''.join(run['text'] for run in text_runs(captured))


def start():
    if alive():
        if tmux('display-message', '-p', '-t', TARGET, '#{pane_dead}').stdout.strip() != '1':
            print('Session already exists. Use screen or attach.')
            return
    # No user SSH configuration, identities, forwards, or external known_hosts writes.
    ssh = ['ssh', '-F', '/dev/null', '-tt',
           '-o', f'UserKnownHostsFile={ROOT / "config/known_hosts"}',
           '-o', 'GlobalKnownHostsFile=/dev/null',
           '-o', 'StrictHostKeyChecking=yes', '-o', 'HostKeyAlgorithms=ssh-ed25519',
           '-o', 'PubkeyAuthentication=no', '-o', 'ServerAliveInterval=30',
           '-o', 'ServerAliveCountMax=3', '-o', 'ConnectTimeout=15',
           'nethack@us.hardfought.org']
    if alive():
        tmux('respawn-pane', '-t', TARGET, *ssh)
    else:
        subprocess.run(['tmux', '-S', SOCKET, '-f', str(ROOT / 'config/tmux.conf'),
                        'new-session', '-d', '-s', 'hardfought', '-x', str(COLS), '-y', str(ROWS),
                        *ssh], check=True)
    tmux('resize-window', '-t', 'hardfought:0', '-x', str(COLS), '-y', str(ROWS))
    time.sleep(1)
    print(screen())


def credentials():
    path = RUNTIME / 'credentials.json'
    if not path.exists():
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as handle:
            json.dump({'username': 'CodexDelver', 'password': secrets.token_hex(10)}, handle)
    return json.loads(path.read_text())


def send(value, named=False, sensitive=False):
    if not alive() or tmux('display-message', '-p', '-t', TARGET, '#{pane_dead}').stdout.strip() == '1':
        raise RuntimeError('No live SSH pane; inspect screen and reconnect.')
    audit.require_healthy()
    visible = (RUNTIME / 'broadcast.enabled').exists() and not sensitive
    before = screen() if visible else '[hidden for privacy]'
    command_id = uuid.uuid4().hex
    turn = re.search(r'\bT:(\d+)', before)
    data = {'command_id': command_id, 'input': value if not sensitive else None,
            'named': named, 'sensitive': sensitive, 'screen_before': before,
            'game_turn': int(turn[1]) if turn else None, 'source': 'session.py'}
    audit.record('input_requested', data)  # durable intent BEFORE input reaches SSH
    try:
        # tmux parses a standalone semicolon as a command separator even when
        # passed as one argv element. Send its byte explicitly, not as syntax.
        if value == ';' and not named:
            tmux('send-keys', '-t', TARGET, '-H', '--', '3b')
        else:
            tmux('send-keys', '-t', TARGET, *([] if named else ['-l']), '--', value)
    except Exception:
        audit.record('input_failed', {'command_id': command_id})
        raise
    audit.record('input_queued', {'command_id': command_id})
    if visible and turn:
        label = ('move ' + guard.NAMES[value]) if value in guard.NAMES else {
            '<': 'go upstairs', '>': 'go downstairs', 's': 'search', 'i': 'inspect inventory',
            'S': 'save game', ',': 'pick up', '.': 'wait'}.get(value, 'game input')
        audit.publish('command', value, label=label, named=named, game_turn=int(turn[1]), command_id=command_id)


def snapshot():
    hidden = not (RUNTIME / 'broadcast.enabled').exists()
    note = RUNTIME / 'commentary.txt'
    runs = text_runs('Preparing the expedition.\nThe game will appear here shortly.' if hidden else screen(ansi=True))
    activity = audit.public_state()
    if hidden:
        activity['feed'] = []
    return {'screen': ''.join(run['text'] for run in runs), 'runs': runs, 'cols': COLS, 'rows': ROWS,
            'commentary': note.read_text() if note.exists() else 'Setting up camp at the dungeon entrance.',
            'visible': not hidden, 'updated': datetime.now(timezone.utc).isoformat(), **activity}


def print_screen(compact=False):
    current = screen()
    if (RUNTIME / 'audit-active.json').exists():
        audit.record('agent_observation', {'screen': current if (RUNTIME / 'broadcast.enabled').exists()
                     else '[hidden for privacy]', 'compact_display': compact})
    if compact:
        cursor = tmux('display-message', '-p', '-t', TARGET, '#{cursor_x},#{cursor_y}').stdout.strip()
        print(f'Terminal cursor (x,y; usually hero when no menu): {cursor}')
        print('\n'.join(f'{row:02d} {line[:82]}' for row, line in enumerate(current.splitlines())
                        if line[:82].strip(' │─┌┐└┘')))
        features = [f'{char}@{col},{row}'
                    for row, line in enumerate(current.splitlines()) if 10 <= row <= 30
                    for col, char in enumerate(line[:81])
                    if char not in ' │─┌┐└┘·.▒}']
        print('Map features (x,y): ' + ' '.join(features))
        lines = current.splitlines()
        for row, line in enumerate(lines):
            if not 10 <= row <= 30:
                continue
            for col, char in enumerate(line[:81]):
                if char != '@':
                    continue
                neighbors = []
                for key, dx, dy in [('7', -1, -1), ('8', 0, -1), ('9', 1, -1),
                                    ('4', -1, 0), ('6', 1, 0),
                                    ('1', -1, 1), ('2', 0, 1), ('3', 1, 1)]:
                    y, x = row + dy, col + dx
                    if 0 <= y < len(lines) and 0 <= x < len(lines[y]):
                        cell = lines[y][x]
                        neighbors.append(f'{key}:{cell if cell != " " else "blank"}({x},{y})')
                print(f'Neighbors of @({col},{row}): ' + ' '.join(neighbors))
    else:
        print(current, end='')


def stash_gold(bag, expected_gold):
    """One inventory action, with checked menu transitions and no blind macro."""
    initial = guard.state(*guard.observe(sys.modules[__name__]))
    if initial is None or expected_gold <= 0:
        raise RuntimeError('Stash requires a recognized map and positive expected gold.')
    gold = re.search(r'(?:\$|\*):(\d+)', initial['status'])
    if (not gold or int(gold[1]) != expected_gold
            or any(word in initial['status'] for word in guard.DANGERS)
            or initial['hp'] * 3 < initial['max_hp'] * 2):
        raise RuntimeError('Stash gold count, health, or condition preflight failed.')
    reason = f'Stash {expected_gold} loose gold in the holding bag; verify each menu before continuing.'
    audit.record('public_decision', {'text': reason})
    audit.publish('decision', reason, source='checked inventory action')

    def transition(keys, expected, final=False):
        send(keys)
        observed = guard.settled(sys.modules[__name__])
        audit.record('stash_gold_step', {'input': keys, 'observation': None if observed is None else {
            'screen': observed[0], 'cursor': observed[1], 'pets': sorted(observed[2])}})
        if observed is None:
            raise RuntimeError('Stash stopped: terminal did not settle. Inspect screen.')
        current, cursor, _ = observed
        rows = current.splitlines()
        # Only the actual game panel, never the permanent inventory sidebar.
        panel = '\n'.join(row[:81] for row in rows)
        status = rows[34][:81] if len(rows) > 34 else ''
        if expected not in panel:
            raise RuntimeError('Stash stopped: unexpected menu or confirmation. Inspect screen.')
        if final:
            after = guard.state(*observed)
            if (after is None or after['position'] != initial['position']
                    or after['level'] != initial['level']
                    or not re.search(r'(?:\$|\*):0\b', status)):
                raise RuntimeError('Stash stopped: final map or zero-gold state unverified.')
        elif status != initial['status'] or not (0 <= cursor[1] <= 10):
            raise RuntimeError('Stash stopped: game advanced or unexpected cursor. Inspect screen.')
        return panel

    panel = transition('a' + bag, 'Do what with your bag called HOLDING?')
    if 's) stash one item into the bag' not in panel:
        raise RuntimeError('Stash stopped: stash menu option missing.')
    panel = transition('s', 'What do you want to stash? [$')
    transition('$', f'You put {expected_gold} gold pieces into the bag called HOLDING.', final=True)
    print_screen(True)


def wrest_wish(letter, x, y, limit):
    """Retry a manually verified empty wishing wand; stop on any changed situation."""
    initial_hp = None
    previous_turn = None
    unchanged = 0
    for attempt in range(min(max(limit, 0), 20) + 1):
        current = screen()
        lines = current.splitlines()
        hp = re.search(r'HP:(\d+)\(', current)
        turn = re.search(r'T:(\d+)', current)
        cursor = tmux('display-message', '-p', '-t', TARGET,
                      '#{cursor_x},#{cursor_y}').stdout.strip()
        messages = [line[:82].strip(' │') for line in lines[1:8] if line[:82].strip(' │')]
        if (not hp or not turn or cursor != f'{x},{y}' or len(lines) < 35
                or lines[y][x:x+1] != '@' or not messages
                or not messages[-1].endswith('Nothing happens.')):
            print('Stopped: prompt, message, or position changed.')
            break
        hp, turn = int(hp[1]), int(turn[1])
        initial_hp = hp if initial_hp is None else initial_hp
        unchanged = unchanged + 1 if turn == previous_turn else 0
        if hp < initial_hp or unchanged >= 3 or any(
                word in lines[34] for word in ('Hungry', 'Weak', 'Faint', 'Blind', 'Conf', 'Stun')):
            print('Stopped: damage, condition, or no turn advancement.')
            break
        nearby = ''.join(lines[row][max(0, x-4):x+5]
                         for row in range(max(10, y-4), min(31, y+5)))
        if any(char.isalpha() or char in '&12345' for char in nearby) or nearby.count('@') != 1:
            print('Stopped: nearby monster or warning.')
            break
        if attempt == min(max(limit, 0), 20):
            print(f'Stopped after {attempt} attempts.')
            break
        previous_turn = turn
        send('z' + letter)
        time.sleep(1)
    print_screen(True)


def wait_pets(x, y, limit):
    """Bounded search turns at a manually verified safe rendezvous; never move."""
    previous_turn = None
    initial_hp = None
    initially_blind = 'Blind' in screen().splitlines()[-2]
    for attempt in range(min(max(limit, 0), 25) + 1):
        current = screen()
        lines = current.splitlines()
        hp = re.search(r'HP:(\d+)\(', current)
        turn = re.search(r'T:(\d+)', current)
        if not hp or not turn or y >= len(lines) or lines[y][x:x+1] != '@':
            print('Stopped: position/status not recognized.')
            break
        hp, turn = int(hp[1]), int(turn[1])
        initial_hp = hp if initial_hp is None else initial_hp
        if hp < initial_hp or turn == previous_turn or any(word in lines[34] for word in ('Weak', 'Faint', 'Conf', 'Stun')) or ('Blind' in lines[34] and not initially_blind):
            print('Stopped: damage, condition, or no turn advancement.')
            break
        nearby = ''.join(lines[row][max(0, x-1):x+2] for row in range(max(10, y-1), min(31, y+2)))
        if 'f' in nearby and 'u' in nearby:
            print(f'Both expected pet glyphs adjacent after {attempt} waiting turns; inspect before stairs.')
            break
        if any(char.isalpha() and char not in 'fu' for char in nearby):
            print('Stopped: another adjacent monster glyph.')
            break
        if attempt == min(max(limit, 0), 25):
            print('Stopped: waiting turn limit.')
            break
        previous_turn = turn
        send('s')
        time.sleep(1)
    print_screen(True)


class Viewer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            body = (ROOT / 'web/index.html').read_bytes()
            mime = 'text/html; charset=utf-8'
        elif self.path == '/state':
            body = json.dumps(snapshot()).encode()
            mime = 'application/json'
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('start', 'screen', 'attach', 'hide', 'show', 'viewer'):
        item = sub.add_parser(name)
        if name == 'screen':
            item.add_argument('--compact', action='store_true')
    keys = sub.add_parser('keys', help='Literal keystrokes, or tmux names with --named')
    keys.add_argument('value')
    keys.add_argument('--named', action='store_true')
    keys.add_argument('--compact', action='store_true')
    keys.add_argument('--why', help='Brief public rationale, recorded before these inputs')
    keys.add_argument('--raw', action='store_true', help='Explicit bypass for menu input, recorded in the audit')
    keys.add_argument('--settle', type=float, default=1,
                      help='Seconds to allow terminal animations to finish (0–10)')
    stash = sub.add_parser('stash-gold', help='One checked bag action; stop on unexpected menus or gold count')
    stash.add_argument('--bag', required=True, choices=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    stash.add_argument('--expected-gold', required=True, type=int)
    pets = sub.add_parser('wait-pets', help='At a verified safe tile, search up to 25 turns for adjacent f and u')
    pets.add_argument('x', type=int)
    pets.add_argument('y', type=int)
    pets.add_argument('--limit', type=int, default=20)
    wrest = sub.add_parser('wrest-wish', help='Guarded retries of a verified empty wishing wand')
    wrest.add_argument('letter', choices=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    wrest.add_argument('x', type=int)
    wrest.add_argument('y', type=int)
    wrest.add_argument('--limit', type=int, default=20)
    secret = sub.add_parser('credential', help='Send a credential without printing or logging it')
    secret.add_argument('field', choices=['username', 'password'])
    note = sub.add_parser('note', help='Set public stream commentary')
    note.add_argument('text')
    serve = sub.add_parser('serve')
    serve.add_argument('--port', type=int, default=8766)
    serve.add_argument('--host', default='0.0.0.0')
    args = parser.parse_args()
    RUNTIME.mkdir(mode=0o700, exist_ok=True)
    if args.command == 'start':
        start()
    elif args.command == 'screen':
        print_screen(args.compact)
    elif args.command == 'attach':
        os.execvp('tmux', ['tmux', '-S', SOCKET, 'attach-session', '-r', '-t', 'hardfought'])
    elif args.command == 'keys':
        if not args.named and not args.raw and len(args.value) > 1:
            observed = guard.observe(sys.modules[__name__])
            reason = guard.command_preflight(guard.state(*observed), args.value)
            if reason:
                audit.record('input_preflight_rejected', {
                    'input': args.value, 'reason': reason, 'cursor': observed[1],
                    'screen': observed[0] if (RUNTIME / 'broadcast.enabled').exists() else '[hidden for privacy]',
                })
                raise RuntimeError(reason)
        if args.why:
            audit.record('public_decision', {'text': args.why})
            audit.publish('decision', args.why, source='before command')
        if not args.named and not args.raw and re.fullmatch(r'[12346789]{2,}', args.value):
            guard.walk(sys.modules[__name__], args.value)
        else:
            if not args.raw and re.fullmatch(r'(F[12346789]){2,}', args.value):
                raise RuntimeError('Repeated combat input must be inspected between attacks.')
            if args.raw:
                audit.record('raw_input_override', {'reason': args.why, 'input': args.value})
            send(args.value, args.named)
            time.sleep(min(10, max(0, args.settle)))
            print_screen(args.compact)
    elif args.command == 'stash-gold':
        stash_gold(args.bag, args.expected_gold)
    elif args.command == 'wait-pets':
        wait_pets(args.x, args.y, args.limit)
    elif args.command == 'wrest-wish':
        wrest_wish(args.letter, args.x, args.y, args.limit)
    elif args.command == 'credential':
        if (RUNTIME / 'broadcast.enabled').exists():
            raise RuntimeError('Hide the broadcast before entering credentials.')
        prompt = screen().lower()
        expected = ('username',) if args.field == 'username' else ('password', 'and again')
        if 'logged in as:' in prompt or not any(word in prompt for word in expected):
            raise RuntimeError('Expected credential prompt is not visible; inspect screen first.')
        send(credentials()[args.field], sensitive=True)
        send('Enter', named=True, sensitive=True)
        time.sleep(1)
        print('Credential sent; inspect the next prompt with screen.')
    elif args.command == 'note':
        audit.record('public_decision', {'text': args.text})
        audit.publish('decision', args.text, source='stream note')
        (RUNTIME / 'commentary.txt').write_text(audit.clean(args.text, public=True) + '\n')
    elif args.command == 'hide':
        (RUNTIME / 'broadcast.enabled').unlink(missing_ok=True)
    elif args.command == 'show':
        (RUNTIME / 'broadcast.enabled').touch()
    elif args.command == 'serve':
        print(f'Broadcast view listening on {args.host}:{args.port}', flush=True)
        ThreadingHTTPServer((args.host, args.port), Viewer).serve_forever()
    elif args.command == 'viewer':
        if tmux('has-session', '-t', 'viewer', check=False).returncode == 0:
            if tmux('display-message', '-p', '-t', 'viewer:0.0', '#{pane_dead}').stdout.strip() == '1':
                tmux('respawn-pane', '-t', 'viewer:0.0', sys.executable, str(Path(__file__).resolve()), 'serve')
        else:
            tmux('new-session', '-d', '-s', 'viewer', sys.executable, str(Path(__file__).resolve()), 'serve')
        print('Broadcast view: http://<this-machine>:8766 (all interfaces)')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
