import unittest
from types import SimpleNamespace
from contextlib import ExitStack
from unittest.mock import patch

import session


class LiteralInputTests(unittest.TestCase):
    def test_standalone_semicolon_is_sent_as_hex_byte(self):
        with patch.object(session, 'alive', return_value=True), \
             patch.object(session, 'tmux', return_value=SimpleNamespace(stdout='0')) as tmux, \
             patch.object(session, 'RUNTIME'), \
             patch.object(session, 'screen', return_value='Dlvl:24 T:12890'), \
             patch.object(session.audit, 'require_healthy'), \
             patch.object(session.audit, 'record') as record, \
             patch.object(session.audit, 'publish'):
            session.send(';')
            tmux.assert_called_with('send-keys', '-t', session.TARGET, '-H', '--', '3b')
            self.assertEqual(record.call_args_list[0].args[0], 'input_requested')
            self.assertEqual(record.call_args_list[0].args[1]['input'], ';')
            self.assertEqual(record.call_args_list[-1].args[0], 'input_queued')


class PromptSafetyTests(unittest.TestCase):
    def test_cli_rejects_macro_before_dispatch_from_popup(self):
        with patch('sys.argv', ['session.py', 'keys', 'E-Elbereth\n']), \
             patch.object(session, 'RUNTIME'), \
             patch.object(session.guard, 'observe', return_value=('Things that are here:', (78, 3), frozenset())), \
             patch.object(session.audit, 'record') as record, \
             patch.object(session, 'send') as send:
            with self.assertRaisesRegex(RuntimeError, 'recognized map prompt'):
                session.main()
            send.assert_not_called()
            self.assertEqual(record.call_args.args[0], 'input_preflight_rejected')


def stash_screen(text='', *, gold=290, turn=100, hp=86, cursor=(20, 20), extra=''):
    rows = [' ' * 144 for _ in range(36)]
    for number, line in enumerate(text.splitlines(), 1):
        rows[number] = line.ljust(144)
    rows[20] = ' ' * 20 + '@' + ' ' * 123
    rows[34] = f'Dlvl:16 $:{gold} HP:{hp}(86) T:{turn} {extra}'.ljust(144)
    return ('\n'.join(rows), cursor, frozenset())


class StashGoldTests(unittest.TestCase):
    def run_stash(self, replies, initial=None, expected=290):
        with ExitStack() as stack:
            stack.enter_context(patch.object(session.guard, 'observe', return_value=initial or stash_screen()))
            stack.enter_context(patch.object(session.guard, 'settled', side_effect=replies))
            sent = stack.enter_context(patch.object(session, 'send'))
            stack.enter_context(patch.object(session.audit, 'record'))
            stack.enter_context(patch.object(session.audit, 'publish'))
            stack.enter_context(patch.object(session, 'print_screen'))
            try:
                session.stash_gold('i', expected)
                error = None
            except RuntimeError as exc:
                error = str(exc)
            return [call.args[0] for call in sent.call_args_list], error

    def menus(self):
        return [
            stash_screen('Do what with your bag called HOLDING?\ns) stash one item into the bag', cursor=(55, 10)),
            stash_screen('What do you want to stash? [$ap or ?*]', cursor=(40, 7)),
            stash_screen('You put 290 gold pieces into the bag called HOLDING.', gold=0, turn=101),
        ]

    def test_verified_single_inventory_action(self):
        sent, error = self.run_stash(self.menus())
        self.assertEqual(sent, ['ai', 's', '$'])
        self.assertIsNone(error)

    def test_wrong_gold_or_condition_sends_nothing(self):
        for initial in [stash_screen(gold=291), stash_screen(extra='Stun'), stash_screen(hp=20)]:
            with self.subTest(initial=initial[-2]):
                sent, error = self.run_stash([], initial)
                self.assertEqual(sent, [])
                self.assertIsNotNone(error)

    def test_wrong_container_stops_after_apply(self):
        sent, error = self.run_stash([stash_screen('Do what with your bag?', cursor=(55, 10))])
        self.assertEqual(sent, ['ai'])
        self.assertIn('unexpected menu', error)

    def test_missing_stash_option_stops(self):
        sent, error = self.run_stash([stash_screen('Do what with your bag called HOLDING?', cursor=(55, 10))])
        self.assertEqual(sent, ['ai'])
        self.assertIn('option missing', error)

    def test_changed_game_state_in_menu_stops(self):
        menus = self.menus()
        menus[0] = stash_screen('Do what with your bag called HOLDING?\ns) stash one item into the bag', turn=101, cursor=(55, 10))
        sent, error = self.run_stash(menus)
        self.assertEqual(sent, ['ai'])
        self.assertIn('game advanced', error)

    def test_unexpected_second_prompt_never_sends_gold(self):
        menus = self.menus()
        menus[1] = stash_screen('What do you want to eat?', cursor=(30, 7))
        sent, error = self.run_stash(menus)
        self.assertEqual(sent, ['ai', 's'])
        self.assertIn('unexpected menu', error)

    def test_unsettled_terminal_stops(self):
        sent, error = self.run_stash([None])
        self.assertEqual(sent, ['ai'])
        self.assertIn('did not settle', error)

    def test_final_confirmation_and_zero_gold_required(self):
        for final in [stash_screen(gold=0),
                      stash_screen('You put 290 gold pieces into the bag called HOLDING.', gold=290)]:
            menus = self.menus()
            menus[2] = final
            sent, error = self.run_stash(menus)
            self.assertEqual(sent, ['ai', 's', '$'])
            self.assertIsNotNone(error)


if __name__ == '__main__':
    unittest.main()
