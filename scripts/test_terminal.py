import unittest
from terminal import text_runs


class TerminalColorTests(unittest.TestCase):
    def test_foreground_background_bold_and_resets(self):
        runs = text_runs('\x1b[31m@\x1b[1mD\x1b[22;44mx\x1b[39;49m.')
        self.assertEqual(runs, [
            {'text': '@', 'fg': '#cd0000'},
            {'text': 'D', 'fg': '#ff0000', 'bold': True},
            {'text': 'x', 'fg': '#cd0000', 'bg': '#0000ee'},
            {'text': '.'}])

    def test_extended_colors(self):
        runs = text_runs('\x1b[38;5;172mA\x1b[48;2;10;20;30mB\x1b[0mC')
        self.assertEqual(runs[0]['fg'], '#d78700')
        self.assertEqual(runs[1]['bg'], '#0a141e')
        self.assertEqual(runs[2], {'text': 'C'})

    def test_geometry_and_literal_markup_survive(self):
        text = '  <script>alert(1)</script> & "\n @  #\n'
        runs = text_runs('\x1b[32m' + text + '\x1b[0m')
        self.assertEqual(''.join(run['text'] for run in runs), text)

    def test_inverse_and_full_reset(self):
        runs = text_runs('\x1b[7;4m@\x1b[0m.')
        self.assertEqual(runs[0], {'text': '@', 'fg': '#0a1012', 'bg': '#e5e5e5', 'underline': True})
        self.assertEqual(runs[1], {'text': '.'})

    def test_truncated_extended_color_is_ignored(self):
        self.assertEqual(text_runs('\x1b[38;2;255m@'), [{'text': '@'}])

    def test_curses_line_drawing_and_text_use_separate_charsets(self):
        runs = text_runs('\x0elqqk\nxa~x\x1b[31mq\x1b[0mq\x0f liquid')
        self.assertEqual(''.join(run['text'] for run in runs), '┌──┐\n│▒·│── liquid')
        self.assertEqual(runs[1]['fg'], '#cd0000')


if __name__ == '__main__':
    unittest.main()
