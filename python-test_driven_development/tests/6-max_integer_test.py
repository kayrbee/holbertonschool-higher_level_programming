#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertTrue(max_integer([1, 2, 3, 4]))
