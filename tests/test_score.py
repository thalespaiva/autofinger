#!/usr/bin/python3

import unittest


from score import Score


class ScoreTest(unittest.TestCase):

    def test_parse_small_portion_of_inventio1(self):
        s = Score.parse('tests/test_files/jsbach_inventio1.xml')
        self.assertEqual(s.title, 'Inventio I')
        self.assertEqual(s.author, 'J. S. Bach')
        self.assertEqual(len(s.lines), 1)
        self.assertEqual(len(s.lines[0]), 7)
        print(s)

    def test_get_units_of_inventio1(self):
        s = Score.parse('tests/test_files/jsbach_inventio1.xml')

        for unit in s.get_units():
            print(unit)


if __name__ == "__main__":
    unittest.main()
