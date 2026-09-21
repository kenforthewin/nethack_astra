"""Conservative movement batching over visible terminal state, not a game oracle."""
import re
import time
from terminal import text_runs

MOVES = {'1': (-1, 1), '2': (0, 1), '3': (1, 1), '4': (-1, 0),
         '6': (1, 0), '7': (-1, -1), '8': (0, -1), '9': (1, -1)}
NAMES = {'1': 'southwest', '2': 'south', '3': 'southeast', '4': 'west',
         '6': 'east', '7': 'northwest', '8': 'north', '9': 'northeast'}
DANGERS = ('Slime', 'Stone', 'Ill', 'FoodPois', 'TermIll', 'Stun', 'Conf',
           'Blind', 'Hallu', 'Weak', 'Faint', 'Hungry', 'Strngl', 'Held')


def command_preflight(s, value, named=False, raw=False):
    """A literal macro needs a map prompt, unless explicitly reviewed as menu input."""
    if not named and not raw and len(value) > 1 and s is None:
        return 'Multi-key input requires a recognized map prompt. Dismiss the popup first, or use --raw only for a reviewed menu response.'
    return None


def state(screen, cursor, pets=()):
    rows = screen.splitlines()
    x, y = cursor
    status = rows[34][:81] if len(rows) > 34 else ''
    hp = re.search(r'HP:(\d+)\((\d+)\)', status)
    turn = re.search(r'T:(\d+)', status)
    level = re.search(r'Dlvl:(\d+)', status)
    home = re.match(r'^\s*│?\s*Home ([1-9]\d*)\s', status)
    plane = re.match(r'^\s*│?\s*(Earth|Air|Fire|Water|Astral)\s', status)
    if not hp or not turn or not (level or home or plane) or not (10 <= y <= 30 and 0 <= x < 81):
        return None
    # The configured player glyph changes when polymorphed. Recognize only
    # this verified form, requiring both its title and monster status, rather
    # than accepting any monster under the cursor as the player.
    gray_dragon = (len(rows) > 33 and 'the Gray Dragon' in rows[33][:81]
                   and re.search(r'\bHD:15\b', status) is not None)
    player_glyph = 'D' if gray_dragon else '@'
    if len(rows[y]) <= x or rows[y][x] != player_glyph:
        return None
    return {'rows': rows, 'position': cursor, 'hp': int(hp[1]), 'max_hp': int(hp[2]),
            'turn': int(turn[1]),
            'level': int(level[1]) if level else ('Home:' + home[1] if home else 'Plane:' + plane[1]),
            'status': status, 'pets': pets}


def preflight(s, key):
    if s is None:
        return 'Not at a recognized map input prompt.'
    if any(word in s['status'] for word in DANGERS):
        return 'Condition requires attention.'
    if s['hp'] * 3 < s['max_hp'] * 2:
        return 'Health below two-thirds.'
    x, y = s['position']
    for row in range(max(10, y-2), min(31, y+3)):
        for col in range(max(1, x-2), min(80, x+3)):
            if (col, row) == (x, y):
                continue
            if (col, row) in s.get('pets', ()):
                continue  # explicit hilite_pet display, not a glyph whitelist
            char = s['rows'][row][col:col+1]
            if char and (char.isalpha() or char in "@&12345;:'"):
                return 'Nearby creature or warning; inspect before continuing.'
    dx, dy = MOVES[key]
    nx, ny = x + dx, y + dy
    if not (1 <= nx < 80 and 10 <= ny <= 30):
        return 'Map edge.'
    # Rogue-style levels use ASCII '.' instead of the configured middot floor.
    if s['rows'][ny][nx:nx+1] not in '▒·.#<>$%!?=()[/*`"_':
        return 'Next tile is unknown, blocked, a door, water, or a trap.'
    return None


def changed(before, after, key):
    if after is None:
        return 'Unexpected prompt or unrecognized state.'
    if after['hp'] < before['hp']:
        return 'Damage taken.'
    # Natural healing can hide trap damage in the net HP change (run3 D41,
    # T31715..31724). Compare visible message counts, not the lingering history,
    # and join wrapped lines so the observed falling-rock message still matches.
    def falling_rocks(s):
        text = ' '.join(row[:81].strip(' │') for row in s['rows'][:8])
        return ' '.join(text.lower().split()).count('a rock falls on your head')
    if falling_rocks(after) > falling_rocks(before):
        return 'New falling-rock trap message; inspect before continuing.'
    if after['level'] != before['level']:
        return 'Dungeon level changed.'
    dx, dy = MOVES[key]
    x, y = before['position']
    if after['position'] != (x+dx, y+dy):
        return 'Movement did not match the planned step.'
    if after['turn'] - before['turn'] > 2:
        return 'Unexpected time advancement.'
    if any(word in after['status'] for word in DANGERS):
        return 'New or ongoing condition requires attention.'
    return None


def observe(session):
    runs = text_runs(session.screen(ansi=True))
    screen = ''.join(run['text'] for run in runs)
    pets = set()
    x = y = 0
    for run in runs:
        for char in run['text']:
            if char == '\n':
                x = 0
                y += 1
                continue
            # The configured curses hilite_pet renders reverse video. Do not
            # confuse ordinary f/d glyphs or inverse item piles with a pet.
            if (10 <= y <= 30 and 1 <= x < 80 and (char.isalpha() and char != 'I' or char in "@&:;'")
                    and run.get('fg') == '#0a1012' and run.get('bg')):
                pets.add((x, y))
            x += 1
    cursor = tuple(map(int, session.tmux('display-message', '-p', '-t', session.TARGET,
                                        '#{cursor_x},#{cursor_y}').stdout.strip().split(',')))
    return screen, cursor, frozenset(pets)


def settled(session):
    start = last_change = time.monotonic()
    previous = observe(session)
    while time.monotonic() - start < 4:
        time.sleep(.15)
        current = observe(session)
        if current != previous:
            last_change = time.monotonic()
            previous = current
        if time.monotonic() - start >= .75 and time.monotonic() - last_change >= .3:
            return current
    return None


def walk(session, keys):
    if not keys or len(keys) > 24 or any(key not in MOVES for key in keys):
        raise RuntimeError('Guarded walking accepts 1–24 movement digits, excluding 5.')
    completed = 0
    reason = None
    for key in keys:
        before = state(*observe(session))
        reason = preflight(before, key)
        if reason:
            break
        session.send(key)
        observed = settled(session)
        if observed is None:
            reason = 'Terminal did not settle; inspect animations or prompts.'
            break
        after = state(*observed)
        reason = changed(before, after, key)
        session.audit.record('guarded_step', {'key': key, 'screen_after': observed[0], 'stop': reason})
        completed += 1
        if reason:
            break
    result = {'requested': keys, 'sent_steps': completed, 'stop': reason or 'Batch complete.'}
    session.audit.record('guarded_batch', result)
    print(result)
    session.print_screen(True)
