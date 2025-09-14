#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([4, 2, 7, 1, 2]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
