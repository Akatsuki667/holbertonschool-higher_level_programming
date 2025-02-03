#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1,-2 ,-3 ,-4]), -1)
        self.assertEqual(max_integer([0,-2 ,-3 ,-4]), 0)

        self.assertEqual(max_integer([3.5, 5.5, 8.9]), 8.9)
        self.assertEqual(max_integer([-3.5, -5.5, -8.9]), -3.5)


    def test_type_errors_raised(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "Hello"])
        self.assertRaises(TypeError, max_integer, ["1", 2, "3"])
