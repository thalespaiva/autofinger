#!/usr/bin/python3

import unittest
import fractions

import note


class TestNote(unittest.TestCase):

    def test_pitch_of_f_sharp_4_is_46(self):
        self.assertEqual(note.Note.get_pitch('F#4'), 46)

    def test_a_sharp_is_a_black_key(self):
        a_sharp_2 = note.Note('A#2', fractions.Fraction(1, 3))

        self.assertTrue(a_sharp_2.is_a_black_key())

    def test_c_is_not_a_black_key(self):
        c_4 = note.Note('C4', fractions.Fraction(1, 2))

        self.assertFalse(c_4.is_a_black_key())

    def test_f_sharp_3_has_the_same_pitch_as_F_sharp_3_equals_34(self):
        f_sharp_3 = note.Note('f#3', fractions.Fraction(1, 3))
        F_sharp_3 = note.Note('F#3', fractions.Fraction(1, 3))

        self.assertEqual(F_sharp_3.pitch, f_sharp_3.pitch)
        self.assertEqual(f_sharp_3.pitch, 34)

    def test_distance_between_b1_and_g2_is_20(self):
        b_1 = note.Note('b1', fractions.Fraction(1, 2))
        g_2 = note.Note('g2', fractions.Fraction(1, 2))

        self.assertEqual(note.Note.distance(b_1, g_2), 20)


if __name__ == '__main__':
    unittest.main()
