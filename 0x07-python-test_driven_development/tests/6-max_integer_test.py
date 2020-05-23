#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger

    Args:
        unittest (): [description]
    """
    def test_number(self):
        """ Test some values
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([None]), None)
        self.assertNotIsInstance(max_integer("holberton"), int)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, -0, 0]), 0)
        self.assertEqual(max_integer([9, 8, 7, 7]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-2.7, -2.6, -2.5]), -2.5)

    def test_error(self):
        """test posible error
        """
        with self.assertRaises(TypeError):
            max_integer(0)
        with self.assertRaises(TypeError):
            max_integer(100)
