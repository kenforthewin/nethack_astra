import unittest
from unittest.mock import patch
import sokoban


def screen(message, older=''):
    return '\n'.join(['border', older] + [''] * 5 + ['│' + message + '│'] + [''] * 28)


class BystanderTests(unittest.TestCase):
    def test_pet_swaps_never_allow_pushing_creatures(self):
        pet, empty = (2, 1), (3, 1)
        self.assertFalse(sokoban.creature_blocks(pet, None, {pet: 'tame'}, True))
        self.assertTrue(sokoban.creature_blocks(pet, None, {pet: 'tame'}, False))
        self.assertTrue(sokoban.creature_blocks(pet, None, {pet: 'peaceful'}, True))
        self.assertTrue(sokoban.creature_blocks(pet, None, {pet: None}, True))
        self.assertTrue(sokoban.creature_blocks(empty, pet, {pet: 'tame'}, True))

    def test_confirmed_peaceful(self):
        self.assertTrue(sokoban.peaceful_description(
            screen('G        a gnome (peaceful gnomish wizard) [seen: telepathy]'), 'G'))

    def test_hostile_not_accepted_from_old_description(self):
        self.assertFalse(sokoban.peaceful_description(
            screen('G        a gnome (gnome)', 'G a gnome (peaceful gnome)'), 'G'))

    def test_wrong_glyph_or_prompt_rejected(self):
        self.assertFalse(sokoban.peaceful_description(screen('h a humanoid (peaceful dwarf)'), 'G'))
        self.assertFalse(sokoban.peaceful_description(screen('Pick an object.'), 'G'))

    def test_tame_and_wrapped_descriptions(self):
        self.assertTrue(sokoban.peaceful_description(
            screen('W a wraith (tame wraith called Proteus)'), 'W'))
        rows = screen('').splitlines()
        rows[5:8] = ['Pick an object.', 'h a humanoid (peaceful dwarf) [seen: normal', 'vision, infravision]']
        self.assertTrue(sokoban.peaceful_description('\n'.join(rows), 'h'))
        rows[5:8] = ['h a humanoid (peaceful dwarf)', 'Pick an object.', 'h a humanoid (mind flayer)']
        self.assertFalse(sokoban.peaceful_description('\n'.join(rows), 'h'))

    def test_inspection_requires_unchanged_map_status_and_cursor(self):
        before = screen('old message')
        after = screen('G a gnome (peaceful gnome)')
        with patch.object(sokoban.session, 'send') as send, \
             patch.object(sokoban.session.audit, 'record'), \
             patch.object(sokoban.session.guard, 'settled') as settled:
            settled.return_value = (after, (10, 20), frozenset())
            self.assertTrue(sokoban.inspect_peaceful((10, 20), (12, 19), 'G', before))
            send.assert_called_with(';@668.')
            settled.return_value = (after, (11, 20), frozenset())
            self.assertFalse(sokoban.inspect_peaceful((10, 20), (12, 19), 'G', before))
            settled.return_value = (after + 'changed', (10, 20), frozenset())
            self.assertFalse(sokoban.inspect_peaceful((10, 20), (12, 19), 'G', before))


if __name__ == '__main__':
    unittest.main()
