#!/usr/bin/python3

import unittest
from fractions import Fraction

from unit import Unit
from note import Note


class UnitTest(unittest.TestCase):

    ERROR = 0.00001

    def test_a3_b4_c2_is_sorted_to_c2_a3_b4(self):
        a_3 = Note('a3')
        b_4 = Note('b4')
        c_2 = Note('c2')

        u = Unit([a_3, b_4, c_2], Fraction(1, 2))
        print(u)
        self.assertEqual(u.notes, [c_2, a_3, b_4])

    def test_random_unit_is_valid(self):
        r = Unit.random_unit()

        self.assertIsInstance(r, Unit)

    def test_c1_d1_e1_has_center_3(self):
        notes = Note.init_notes(['c1', 'd1', 'e1'])
        unit = Unit(notes, Fraction(2, 4))

        self.assertAlmostEqual(unit.center, 3)

    def test_d_sharp_3_d_2_e_4_has_center_27(self):
        notes = Note.init_notes(['d#3', 'd2', 'e4'])
        unit = Unit(notes, Fraction(2, 4))

        self.assertAlmostEqual(unit.center, 28)


if __name__ == "__main__":
    unittest.main()
