#!/usr/bin/python3

import unittest
from fractions import Fraction


from bar import Bar
from unit import Unit
from note import Note


class BarTest(unittest.TestCase):

    ERROR = 0.00001

    def test_center_and_var1(self):
        chords = [Note.init_notes(['d1', 'e1']),
                  Note.init_notes(['d1', 'e1']),
                  Note.init_notes(['d1', 'e1']),
                  Note.init_notes(['d1', 'e1'])]

        units = [Unit(chord, Fraction(1, 1)) for chord in chords]
        bar = Bar(key='C', time_signature='4/4', units=units)

        self.assertAlmostEqual(bar.center, 4, delta=self.ERROR)
        self.assertAlmostEqual(bar.var, 0, delta=self.ERROR)

    def test_center_and_var2(self):
        chords = [Note.init_notes(['d1', 'e1']),
                  Note.init_notes(['d1', 'f#1']),
                  Note.init_notes(['d1', 'g#1']),
                  Note.init_notes(['d1', 'a#1'])]

        units = [Unit(chord, Fraction(1, 1)) for chord in chords]
        bar = Bar(key='C', time_signature='4/4', units=units)

        self.assertAlmostEqual(bar.center, 5.5, delta=self.ERROR)
        self.assertAlmostEqual(bar.var, 1.25, delta=self.ERROR)

if __name__ == '__main__':
    unittest.main()
