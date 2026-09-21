#!/usr/bin/env python3
"""Read-only route proposal over the currently remembered terminal map."""
import argparse
import collections
import json
import session

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('x', type=int)
p.add_argument('y', type=int)
p.add_argument('--limit', type=int, default=20)
p.add_argument('--allow-traps', action='store_true', help='Include trap tiles; caller must verify each is safe')
args = p.parse_args()
rows = session.screen().splitlines()
start = tuple(map(int, session.tmux('display-message', '-p', '-t', session.TARGET,
                                  '#{cursor_x},#{cursor_y}').stdout.strip().split(',')))
goal = (args.x, args.y)
floor = set('▒·<>$%!?=()[/*`"_')
if args.allow_traps:
    floor.add('^')
directions = [('8', 0, -1), ('6', 1, 0), ('2', 0, 1), ('4', -1, 0),
              ('9', 1, -1), ('3', 1, 1), ('1', -1, 1), ('7', -1, -1)]

def tile(pos):
    x, y = pos
    return rows[y][x] if 1 <= x < 80 and 11 <= y <= 30 else ' '

def walkable(pos):
    return pos == start or tile(pos) in floor or tile(pos) in '-|'

if tile(start) != '@':
    raise SystemExit('No hero at the terminal cursor; inspect the active prompt.')
todo = collections.deque([start])
previous = {start: None}
while todo:
    current = todo.popleft()
    if current == goal:
        break
    for key, dx, dy in directions:
        nxt = (current[0] + dx, current[1] + dy)
        if nxt in previous or not walkable(nxt):
            continue
        if dx and dy:
            if tile(current) in '-|' or tile(nxt) in '-|':
                continue
            # A boulder or monster beside a diagonal is not a rock wall.
            # In particular, the known boulder bypass on D51 is legal.
            if (tile((current[0] + dx, current[1])) == ' '
                    and tile((current[0], current[1] + dy)) == ' '):
                continue
        previous[nxt] = (current, key)
        todo.append(nxt)
if goal not in previous:
    raise SystemExit('No fully remembered unoccupied route. Inspect monsters, traps, or unknown terrain.')
path = []
current = goal
while current != start:
    before, key = previous[current]
    path.append((key, current))
    current = before
path.reverse()
chunk = path[:max(0, args.limit)]
print(json.dumps({'start': start, 'goal': goal, 'steps': len(path),
                  'keys': ''.join(key for key, pos in chunk),
                  'end': chunk[-1][1] if chunk else start,
                  'traps': [pos for key, pos in chunk if tile(pos) == '^'],
                  'warning': 'Proposal only: excludes known traps, water, boulders, and occupied tiles; does not predict monster movement.'}))
