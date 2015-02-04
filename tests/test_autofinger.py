#!/usr/bin/python

import unittest

from autofinger import ComfortCalculator


class AutofingerTest(unittest.TestCase):

    ERROR = 0.01

    def test_calculate_jump_comfort_1_to_2_jumping_5_is_2_92199(self):
        comfort = ComfortCalculator.calculate_jump_comfort(1, 2, 5)
        self.assertAlmostEqual(comfort, 2.9219999999999997, delta=self.ERROR)


if __name__ == '__main__':
    unittest.main()
