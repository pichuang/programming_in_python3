#!/usr/bin/env python
import unittest

from DP_Strategy.strategy import *


class TestStrategy(unittest.TestCase):
    # TODO Find how to assert stdout/stderr in python
    def test_level_0(self):
        level0 = Strategy()
        level0.execute()

    def test_level_1(self):
        level1 = Strategy(execute_replacement_execute_1)
        level1.name = 'gg'
        level1.execute()

    def test_level_2(self):
        level2 = Strategy(execute_replacement_execute_2)
        level2.name = 'yy'
        level2.execute()


if __name__ == '__main__':
    unittest.main()
