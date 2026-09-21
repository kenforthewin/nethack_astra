"""Convert tmux SGR output into text runs; never interpret terminal text as HTML."""
import re

CSI = re.compile(r'\x1b\[([0-9;:]*)([ -/]*[@-~])|([\x0e\x0f])')
# DEC Special Graphics, which tmux capture-pane -e wraps in shift-out/shift-in.
ACS = str.maketrans({'`': '◆', 'a': '▒', 'f': '°', 'g': '±', 'h': '␤',
                    'i': '␋', 'j': '┘', 'k': '┐', 'l': '┌', 'm': '└', 'n': '┼',
                    'o': '⎺', 'p': '⎻', 'q': '─', 'r': '⎼', 's': '⎽', 't': '├',
                    'u': '┤', 'v': '┴', 'w': '┬', 'x': '│', 'y': '≤', 'z': '≥',
                    '{': 'π', '|': '≠', '}': '£', '~': '·'})
PALETTE = ('#000000', '#cd0000', '#00cd00', '#cdcd00', '#0000ee', '#cd00cd',
           '#00cdcd', '#e5e5e5', '#7f7f7f', '#ff0000', '#00ff00', '#ffff00',
           '#5c5cff', '#ff00ff', '#00ffff', '#ffffff')


def indexed_color(index):
    if not 0 <= index <= 255:
        return None
    if index < 16:
        return PALETTE[index]
    if index >= 232:
        value = 8 + (index - 232) * 10
        return f'#{value:02x}{value:02x}{value:02x}'
    value = index - 16
    levels = (0, 95, 135, 175, 215, 255)
    return '#%02x%02x%02x' % (levels[value // 36], levels[value // 6 % 6], levels[value % 6])


def text_runs(terminal):
    state = {}
    runs = []
    graphics = False

    def append(text):
        if not text:
            return
        if graphics:
            text = text.translate(ACS)
        style = {key: value for key, value in state.items() if key not in ('fg', 'bg', 'reverse')}
        for key in ('fg', 'bg'):
            value = state.get(key)
            if isinstance(value, int):
                if key == 'fg' and value < 8 and state.get('bold'):
                    value += 8
                value = indexed_color(value)
            if value:
                style[key] = value
        if state.get('reverse'):
            style['fg'], style['bg'] = style.get('bg', '#0a1012'), style.get('fg', '#e5e5e5')
        runs.append({'text': text, **style})

    position = 0
    for match in CSI.finditer(terminal):
        append(terminal[position:match.start()])
        position = match.end()
        if match[3]:
            graphics = match[3] == '\x0e'
            continue
        if match[2] != 'm':
            continue
        # tmux emits semicolon SGR parameters for capture-pane -e.
        if ':' in match[1]:
            continue
        codes = [int(value or 0) for value in match[1].split(';')]
        i = 0
        while i < len(codes):
            code = codes[i]
            i += 1
            if code == 0:
                state.clear()
            elif code in (1, 2, 3, 4, 7, 8, 9):
                state[{1: 'bold', 2: 'dim', 3: 'italic', 4: 'underline',
                       7: 'reverse', 8: 'hidden', 9: 'strike'}[code]] = True
            elif code in (22, 23, 24, 27, 28, 29):
                for key in {22: ('bold', 'dim'), 23: ('italic',), 24: ('underline',),
                            27: ('reverse',), 28: ('hidden',), 29: ('strike',)}[code]:
                    state.pop(key, None)
            elif code in (39, 49):
                state.pop('fg' if code == 39 else 'bg', None)
            elif 30 <= code <= 37 or 90 <= code <= 97:
                state['fg'] = code - (30 if code < 90 else 82)
            elif 40 <= code <= 47 or 100 <= code <= 107:
                state['bg'] = code - (40 if code < 100 else 92)
            elif code in (38, 48) and i < len(codes):
                key = 'fg' if code == 38 else 'bg'
                mode = codes[i]
                i += 1
                count = {5: 1, 2: 3}.get(mode, 0)
                values = codes[i:i + count]
                i += count
                if count and len(values) == count and all(0 <= v <= 255 for v in values):
                    state[key] = indexed_color(values[0]) if mode == 5 else '#%02x%02x%02x' % tuple(values)
    append(terminal[position:])
    return runs
