#!/usr/bin/python3

import unittest

import note


class NoteTest(unittest.TestCase):

    ERROR = 0.00001

    def test_pitch_of_f_sharp_4_is_43(self):
        self.assertEqual(note.Note.get_pitch('F#4')[2], 43)

    def test_a_sharp_is_a_black_key(self):
        a_sharp_2 = note.Note('A#2')

        self.assertTrue(a_sharp_2.is_a_black_key())

    def test_c_is_not_a_black_key(self):
        c_4 = note.Note('C4')

        self.assertFalse(c_4.is_a_black_key())

    def test_f_sharp_3_has_the_same_pitch_as_F_sharp_3_equals_31(self):
        f_sharp_3 = note.Note('f#3')
        F_sharp_3 = note.Note('F#3')

        self.assertEqual(F_sharp_3.pitch, f_sharp_3.pitch)
        self.assertEqual(f_sharp_3.pitch, 31)

    def test_distance_between_b1_and_g2_is_20(self):
        b_1 = note.Note('b1')
        g_2 = note.Note('g2')

        self.assertEqual(note.Note.distance(b_1, g_2), 8)

    def test_random_note_is_valid(self):
        r = note.Note.random_note()

        self.assertIsInstance(r, note.Note)

    def test_init_notes_e_1_d_sharp_2_and_f_3(self):
        notes = note.Note.init_notes(['e1', 'd#2', 'f3'])

        self.assertEqual(notes[0].pitch, note.Note('e1').pitch)
        self.assertEqual(notes[1].pitch, note.Note('d#2').pitch)
        self.assertEqual(notes[2].pitch, note.Note('f3').pitch)

    def test_frequency_of_c2_is_approx_65_41(self):
        c2 = note.Note('c2')

        self.assertAlmostEqual(
            c2.get_frequency(), 65.40639132514966, delta=self.ERROR)

    def test_frequency_of_f_sharp_5_is_approx_65_41(self):
        fsharp5 = note.Note('f#5')

        self.assertAlmostEqual(
            fsharp5.get_frequency(), 739.9888454232688, delta=self.ERROR)


if __name__ == '__main__':
    unittest.main()
