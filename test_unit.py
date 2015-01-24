#!/usr/bin/python3

import unittest
from fractions import Fraction

import unit
from note import Note


class UnitTest(unittest.TestCase):

    def test_a3_b4_c2_is_sorted_to_c2_a3_b4(self):
        a_3 = Note('a3')
        b_4 = Note('b4')
        c_2 = Note('c2')

        u = unit.Unit([a_3, b_4, c_2], Fraction(1, 2))
        print(u)
        self.assertEqual(u.notes, [c_2, a_3, b_4])

    def test_random_unit_is_valid(self):
        r = unit.Unit.random_unit()

        self.assertIsInstance(r, unit.Unit)

if __name__ == "__main__":
    unittest.main()
