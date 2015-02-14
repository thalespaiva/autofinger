#!/usr/bin/python

import unittest

from autofingerer import Autofingerer
from score import Score


class AutofingererTest(unittest.TestCase):

    def test_simple_c_scale_fingering(self):
        s = Score.parse('./tests/auxfiles/scale1.xml')
        a = Autofingerer(s)
        self.assertEquals(
            a.find_best_fit_fingering(), [1, 2, 3, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
