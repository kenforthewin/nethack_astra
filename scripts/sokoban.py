#!/usr/bin/env python3
"""Push planner with optional guarded execution for the displayed Sokoban board.

Read-only by default. --execute sends at most 50 checked cardinal steps.
Usage: python3 scripts/sokoban.py X Y PUSHES (r/l/u/d).
"""
import argparse
from collections import deque
import json
import re
import time

import session

DIRECTIONS = {'l': (-1, 0, '4'), 'r': (1, 0, '6'),
              'u': (0, -1, '8'), 'd': (0, 1, '2')}


def add(p, d):
    return p[0] + d[0], p[1] + d[1]


def peaceful_description(screen, glyph):
    """Accept a fresh peaceful/tame farlook, including wrapped descriptions."""
    messages = [row[:82].strip(' │') for row in screen.splitlines()[1:8]]
    boundaries = [i for i, row in enumerate(messages) if row == 'Pick an object.']
    latest = (' '.join(messages[boundaries[-1] + 1:]) if boundaries else
              next((row for row in reversed(messages) if row), ''))
    match = re.match(re.escape(glyph) + r'\s+.*\((peaceful|tame) [^)]*\)', latest)
    return match[1] if match else None


def inspect_peaceful(hero, point, glyph, before):
    dx, dy = point[0] - hero[0], point[1] - hero[1]
    keys = ';@' + ('6' if dx >= 0 else '4') * abs(dx)
    keys += ('2' if dy >= 0 else '8') * abs(dy) + '.'
    session.send(keys)
    observed = session.guard.settled(session)
    accepted = bool(observed and observed[1] == hero
                    and observed[0].splitlines()[10:] == before.splitlines()[10:]
                    and peaceful_description(observed[0], glyph))
    session.audit.record('sokoban_attitude_check', {
        'position': point, 'glyph': glyph, 'confirmed_peaceful': accepted,
        'screen_after': observed[0] if observed else None,
    })
    return peaceful_description(observed[0], glyph) if accepted else None


def creature_blocks(dest, pushed, attitudes, allow_pet_swaps=False):
    return ((dest in attitudes and not (allow_pet_swaps and attitudes[dest] == 'tame'))
            or (pushed is not None and pushed in attitudes))


def route(start, goal, floor, blocked):
    queue = deque([(start, '')])
    seen = {start}
    while queue:
        point, path = queue.popleft()
        if point == goal:
            return path
        for dx, dy, key in DIRECTIONS.values():
            nxt = add(point, (dx, dy))
            if nxt in floor and nxt not in blocked and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + key))
    raise ValueError(f'No safe walking route from {start} to {goal}')


def guarded_execute(sequence, initial_hero, floor, initial_boulders, initial_holes, limit,
                    hidden_holes=(), inspect_bystanders=False, allow_pet_swaps=False):
    """Stop before any further key on monsters, menus, damage, or board mismatch."""
    hero, boulders, holes = initial_hero, set(initial_boulders), set(initial_holes)
    directions = {key: (dx, dy) for dx, dy, key in DIRECTIONS.values()}
    previous_hp = None
    steps = 0
    for key in sequence[:min(max(0, limit), 50)] + '!':
        current = session.screen()
        lines = current.splitlines()
        cursor = tuple(map(int, session.tmux('display-message', '-p', '-t', session.TARGET,
                                            '#{cursor_x},#{cursor_y}').stdout.strip().split(',')))
        # Curses shows a read-only pile description when stepping onto loot.
        # Dismiss only that exact display, never a question or selection menu.
        header = '\n'.join(lines[:9])
        if (cursor[1] < 9 and 'Things that are here:' in header
                and 'Pick up what?' not in header and '[yn' not in header
                and lines[hero[1]][hero[0]] == '@'):
            session.send(' ')
            time.sleep(0.45)
            current = session.screen()
            lines = current.splitlines()
            cursor = tuple(map(int, session.tmux('display-message', '-p', '-t', session.TARGET,
                                                '#{cursor_x},#{cursor_y}').stdout.strip().split(',')))
        cells = {(x, y): c for y, row in enumerate(lines) if 10 <= y <= 30
                 for x, c in enumerate(row[:81]) if 1 <= x <= 79}
        hp_match = re.search(r'HP:(\d+)\(', lines[34])
        hp = int(hp_match[1]) if hp_match else None
        previous_hp = hp if previous_hp is None else previous_hp
        actual_boulders = {p for p, c in cells.items() if c == '0'}
        actual_holes = ({p for p, c in cells.items() if c == '^'}
                        | (set(hidden_holes) & holes))
        if cursor != hero or cells.get(hero) != '@' or actual_boulders != boulders or actual_holes != holes:
            print(f'STOPPED after {steps} steps: board or cursor differs from prediction.')
            break
        max_hp_match = re.search(r'HP:\d+\((\d+)\)', lines[34])
        if (hp is None or hp < previous_hp or not max_hp_match
                or hp * 3 < int(max_hp_match[1]) * 2
                or any(s in lines[34] for s in (*session.guard.DANGERS, 'Burdened'))):
            print(f'STOPPED after {steps} steps: health or condition changed.')
            break
        previous_hp = hp
        monsters = {p: c for p, c in cells.items()
                    if c.isalpha() or c in ":;&'" or (c == '@' and p != hero)}
        attitudes = {}
        if monsters:
            if inspect_bystanders:
                for p, c in monsters.items():
                    attitudes[p] = inspect_peaceful(hero, p, c, current)
                    if not attitudes[p]:
                        break  # Never issue another inspection after a failed one.
            if not inspect_bystanders or not all(attitudes.values()):
                print(f'STOPPED after {steps} steps: monster not confirmed peaceful.')
                break
        if key == '!':
            print(f'Checked {steps} executed steps; remaining keys: {sequence[steps:]}')
            break
        delta = directions[key]
        dest = add(hero, delta)
        if creature_blocks(dest, add(dest, delta) if dest in boulders else None,
                           attitudes, allow_pet_swaps):
            print(f'STOPPED after {steps} steps: creature blocks the next step or push.')
            break
        assert dest in floor and dest not in holes, 'Unsafe walking step'
        if dest in boulders:
            pushed = add(dest, delta)
            assert pushed in floor and pushed not in boulders, 'Unsafe boulder push'
            boulders.remove(dest)
            if pushed in holes:
                holes.remove(pushed)
            else:
                boulders.add(pushed)
        hero = dest
        session.send(key)
        steps += 1
        observed = session.guard.settled(session)
        session.audit.record('sokoban_step', {
            'key': key, 'expected_hero': hero,
            'expected_boulders': sorted(boulders), 'expected_holes': sorted(holes),
            'screen_after': observed[0] if observed else None,
        })
        if observed is None:
            print(f'STOPPED after {steps} steps: terminal did not settle.')
            break
    session.print_screen(True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    parser.add_argument('pushes')
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--max-steps', type=int, default=20)
    parser.add_argument('--inspect-bystanders', action='store_true',
                        help='Farlook every visible creature before every step; only confirmed peaceful or tame bystanders allowed')
    parser.add_argument('--allow-pet-swaps', action='store_true',
                        help='Plan around moving highlighted pets; execute walks into freshly verified tame pets, never push into them')
    parser.add_argument('--hidden-hole', action='append', default=[], metavar='X,Y',
                        help='Known unfilled hole obscured by an item; repeat as needed')
    args = parser.parse_args()
    if args.allow_pet_swaps and not args.inspect_bystanders:
        parser.error('--allow-pet-swaps requires --inspect-bystanders')
    lines = session.screen().splitlines()
    hero = tuple(map(int, session.tmux('display-message', '-p', '-t', session.TARGET,
                                     '#{cursor_x},#{cursor_y}').stdout.strip().split(',')))
    assert lines[hero[1]][hero[0]] == '@', 'Hero cursor not on map; close menu first'
    cells = {(x, y): c for y, row in enumerate(lines) if 10 <= y <= 30
             for x, c in enumerate(row[:81]) if 1 <= x <= 79}
    floor = {p for p, c in cells.items() if c not in ' │─┌┐└┘┬┴├┤┼'}
    boulders = {p for p, c in cells.items() if c == '0'}
    holes = {p for p, c in cells.items() if c == '^'}
    hidden_holes = {tuple(map(int, value.split(','))) for value in args.hidden_hole}
    assert all(p in floor and p not in boulders for p in hidden_holes), 'Invalid hidden hole'
    holes |= hidden_holes
    monsters = {p for p, c in cells.items()
                if c.isalpha() or c in ":;&'" or (c == '@' and p != hero)}
    pets = set(session.guard.observe(session)[2]) if args.allow_pet_swaps else set()
    # This only relaxes the hypothetical plan. Execution re-inspects every
    # creature and always stops before pushing into one, even a tame pet.
    planning_monsters = monsters - pets
    boulder = (args.x, args.y)
    assert boulder in boulders, f'No boulder at {boulder}'
    initial_state = hero, set(boulders), set(holes)
    sequence = ''
    for index, direction in enumerate(args.pushes):
        assert boulder is not None, 'Push sequence continues after filling pit'
        dx, dy, key = DIRECTIONS[direction]
        behind = (boulder[0] - dx, boulder[1] - dy)
        dest = (boulder[0] + dx, boulder[1] + dy)
        assert dest in floor and dest not in boulders | planning_monsters, f'Blocked push to {dest}'
        sequence += route(hero, behind, floor, boulders | holes | planning_monsters) + key
        hero = boulder
        boulders.remove(boulder)
        if dest in holes:
            holes.remove(dest)
            boulder = None
            assert index == len(args.pushes) - 1, 'Push sequence continues after filling pit'
        else:
            boulder = dest
            boulders.add(boulder)
    print(json.dumps({'keys': sequence, 'expected_hero': hero,
                      'expected_boulder': boulder, 'remaining_pits': len(holes)}))
    if args.execute:
        session.audit.record('sokoban_plan', {
            'boulder': [args.x, args.y], 'pushes': args.pushes,
            'keys': sequence, 'max_steps': args.max_steps,
            'inspect_bystanders': args.inspect_bystanders,
            'allow_pet_swaps': args.allow_pet_swaps,
            'initial_highlighted_pets': sorted(pets),
            'initial_hero': initial_state[0],
            'initial_boulders': sorted(initial_state[1]),
            'initial_holes': sorted(initial_state[2]),
        })
        guarded_execute(sequence, initial_state[0], floor, initial_state[1], initial_state[2],
                        args.max_steps, hidden_holes, args.inspect_bystanders, args.allow_pet_swaps)


if __name__ == '__main__':
    main()
