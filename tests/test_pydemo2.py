#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pydemo2
----------------------------------

Tests for `pydemo2` module.
"""

import unittest

from pydemo2 import pydemo2


class TestPydemo2(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        import pydemo2
        assert(pydemo2.pydemo2.greet() == "Hello")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
