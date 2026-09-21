import unittest
from unittest.mock import Mock
import guard


def example():
    rows = [' ' * 144 for _ in range(36)]
    rows[20] = ' ' * 20 + '@▒▒▒▒' + ' ' * 119
    rows[34] = 'Dlvl:1 HP:16(16) T:1'
    return guard.state('\n'.join(rows), (20, 20))


class GuardTests(unittest.TestCase):
    def test_planes_preserve_identity_and_existing_safety_checks(self):
        rows = example()['rows'][:]
        for plane in ('Earth', 'Air', 'Fire', 'Water', 'Astral'):
            with self.subTest(plane=plane):
                rows[34] = f'│{plane}  $:0 HP:192(192) Pw:42(42) AC:-9 Xp:19/2562751 T:36681 │'
                s = guard.state('\n'.join(rows), (20, 20))
                self.assertEqual(s['level'], 'Plane:' + plane)
                self.assertIsNone(guard.command_preflight(s, 'zh'))
                self.assertIsNone(guard.preflight(s, '6'))
                self.assertIn('Health', guard.preflight(dict(s, hp=100), '6'))
                self.assertIn('Condition', guard.preflight(dict(s, status=s['status'] + ' Blind'), '6'))
                self.assertIn('level changed', guard.changed(example(), s, '6'))
                other = 'Air' if plane != 'Air' else 'Earth'
                self.assertIn('level changed', guard.changed(s, dict(s, level='Plane:' + other), '6'))
                self.assertIsNone(guard.state('\n'.join(rows), (21, 20)))
                self.assertIsNone(guard.state('\n'.join(rows), (20, 7)))
                for glyph in (' ', '^', '}', '|', '+'):
                    blocked = rows[:]
                    blocked[20] = blocked[20][:21] + glyph + blocked[20][22:]
                    self.assertIn('unknown, blocked', guard.preflight(guard.state('\n'.join(blocked), (20, 20)), '6'))
                nearby = rows[:]
                nearby[20] = nearby[20][:22] + 'E' + nearby[20][23:]
                self.assertIn('Nearby', guard.preflight(guard.state('\n'.join(nearby), (20, 20)), '6'))
        for status in ('Prompt Earth HP:192(192) T:1', 'Earthquake HP:192(192) T:1',
                       'Other HP:192(192) T:1', 'Earth T:1', 'Earth HP:192(192)'):
            rows[34] = status
            self.assertIsNone(guard.state('\n'.join(rows), (20, 20)))

    def test_quest_home_preserves_branch_identity_and_prompt_checks(self):
        rows = example()['rows'][:]
        for depth in (1, 2):
            rows[34] = f' │Home {depth}  HP:164(164) T:28330 Lev'
            s = guard.state('\n'.join(rows), (20, 20))
            self.assertEqual(s['level'], f'Home:{depth}')
            self.assertIsNone(guard.command_preflight(s, '66'))
            self.assertIsNone(guard.preflight(s, '6'))
            self.assertIn('level changed', guard.changed(example(), s, '6'))
            self.assertIn('level changed', guard.changed(s, dict(s, level='Home:3'), '6'))
            self.assertIsNone(guard.state('\n'.join(rows), (21, 20)))
            self.assertIsNone(guard.state('\n'.join(rows), (20, 7)))
        for status in ('Home 0 HP:16(16) T:1', 'Other 1 HP:16(16) T:1',
                       'Home 1 T:1', 'Home 1 HP:16(16)',
                       'Prompt Home 1 HP:16(16) T:1'):
            rows[34] = status
            self.assertIsNone(guard.state('\n'.join(rows), (20, 20)))

    def test_gray_dragon_requires_title_hd_and_cursor_glyph(self):
        rows = example()['rows'][:]
        rows[20] = rows[20].replace('@', 'D')
        rows[33] = '[CodexDelver the Gray Dragon ] St:18/**'
        rows[34] = 'Dlvl:27 HP:96(96) AC:-1 HD:15 T:24843 Fly'
        s = guard.state('\n'.join(rows), (20, 20))
        self.assertIsNotNone(s)
        self.assertIsNone(guard.command_preflight(s, 'n20s'))
        self.assertIsNone(guard.preflight(s, '6'))
        self.assertIn('Health', guard.preflight(dict(s, hp=60), '6'))
        for index, replacement in [(33, '[CodexDelver the Woman-at-arms]'),
                                   (34, 'Dlvl:27 HP:96(96) Xp:10 T:24843'),
                                   (20, rows[20].replace('D', '@'))]:
            changed = rows[:]
            changed[index] = replacement
            self.assertIsNone(guard.state('\n'.join(changed), (20, 20)))
        self.assertIsNone(guard.state('\n'.join(rows), (21, 20)))
        self.assertIsNone(guard.state('\n'.join(rows), (20, 7)))

    def test_macros_require_map_or_reviewed_menu_override(self):
        self.assertIsNone(guard.command_preflight(example(), 'E-Elbereth\n'))
        self.assertIn('map prompt', guard.command_preflight(None, 'E-Elbereth\n'))
        self.assertIn('map prompt', guard.command_preflight(None, 'Elbereth\n'))
        self.assertIsNone(guard.command_preflight(None, 'Elbereth\n', raw=True))
        self.assertIsNone(guard.command_preflight(None, 'Escape', named=True))
        for key in [' ', '\x1b', 'y', '3']:
            self.assertIsNone(guard.command_preflight(None, key))

    def test_pet_highlight_includes_nonletter_monsters_not_items(self):
        for glyph in "f@&:;'":
            with self.subTest(glyph=glyph):
                session = Mock()
                session.screen.return_value = '\n' * 20 + ' ' * 19 + '\x1b[7m' + glyph + '\x1b[0m'
                session.tmux.return_value.stdout = '20,20'
                self.assertIn((19, 20), guard.observe(session)[2])
                session.screen.return_value = '\n' * 20 + ' ' * 19 + glyph
                self.assertNotIn((19, 20), guard.observe(session)[2])
        for glyph in 'I%!?0':
            session.screen.return_value = '\n' * 20 + ' ' * 19 + '\x1b[7m' + glyph + '\x1b[0m'
            self.assertNotIn((19, 20), guard.observe(session)[2])

    def test_unhighlighted_golem_stops_batch(self):
        s = example()
        s['rows'][20] = s['rows'][20][:19] + "'" + s['rows'][20][20:]
        self.assertIn('Nearby', guard.preflight(s, '6'))

    def test_normal_move(self):
        s = example()
        self.assertIsNone(guard.preflight(s, '6'))
        after = dict(s, position=(21, 20), turn=2)
        self.assertIsNone(guard.changed(s, after, '6'))

    def test_ascii_floor_without_admitting_rogue_walls_or_traps(self):
        for glyph in '.-|+^ }':
            with self.subTest(glyph=glyph):
                s = example()
                s['rows'][20] = s['rows'][20][:21] + glyph + s['rows'][20][22:]
                if glyph == '.':
                    self.assertIsNone(guard.preflight(s, '6'))
                else:
                    self.assertIn('unknown, blocked', guard.preflight(s, '6'))

    def test_monster_stops_batch(self):
        s = example()
        s['rows'][20] = s['rows'][20][:22] + 'P' + s['rows'][20][23:]
        self.assertIn('Nearby', guard.preflight(s, '6'))

    def test_highlighted_pet_does_not_block_distant_step(self):
        s = example()
        s['rows'][20] = s['rows'][20][:19] + 'f' + s['rows'][20][20:]
        s['pets'] = {(19, 20)}
        self.assertIsNone(guard.preflight(s, '6'))
        s['pets'] = set()
        self.assertIn('Nearby', guard.preflight(s, '6'))

    def test_sliming_stops_batch(self):
        s = example()
        self.assertIn('condition', guard.changed(s, dict(s, position=(21, 20), status='Slime'), '6'))

    def test_damage_stops_batch(self):
        s = example()
        self.assertEqual(guard.changed(s, dict(s, hp=15), '6'), 'Damage taken.')

    def test_falling_rock_stops_even_when_healing_masks_damage(self):
        before = example()
        rows = before['rows'][:]
        rows[6] = '│A trap door in the ceiling opens and a rock falls on your│'
        rows[7] = '│head!  Your elven leather helm does not protect you.│'
        for hp in (before['hp'], before['hp'] + 1):
            after = dict(before, rows=rows, position=(21, 20), turn=2, hp=hp)
            self.assertIn('falling-rock', guard.changed(before, after, '6'))

    def test_lingering_falling_rock_message_does_not_stop_new_step(self):
        before = example()
        before['rows'][7] = '│A rock falls on your head!│'
        after = dict(before, position=(21, 20), turn=2)
        self.assertIsNone(guard.changed(before, after, '6'))

    def test_second_visible_falling_rock_message_stops(self):
        before = example()
        before['rows'][6] = '│A rock falls on your head!│'
        rows = before['rows'][:]
        rows[7] = '│A rock falls on your head!│'
        after = dict(before, rows=rows, position=(21, 20), turn=2)
        self.assertIn('falling-rock', guard.changed(before, after, '6'))

    def test_wrong_movement_stops_batch(self):
        s = example()
        self.assertIn('Movement', guard.changed(s, s, '6'))

    def test_unknown_terrain_stops_batch(self):
        self.assertIn('unknown', guard.preflight(example(), '8'))

    def test_prompt_stops_batch(self):
        self.assertIsNone(guard.state('Pick an item?', (8, 1)))
        self.assertIn('prompt', guard.preflight(None, '6'))

    def test_wait_is_not_movement(self):
        with self.assertRaises(RuntimeError):
            guard.walk(None, '555')


if __name__ == '__main__':
    unittest.main()
