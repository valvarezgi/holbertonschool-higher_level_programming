#!/usr/bin/python3
""" TestSquare
"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """TestSquare

    Args:
        unittest ([type]): [description]
    """

    def setUp(self):
        """setUp
        """
        Base._Base__nb_objects = 0
        self.sq1 = Square(5)
        self.sq2 = Square(1, 5)
        self.sq3 = Square(3, 4, 5)
        self.sq4 = Square(2, 3, 4, 5)

    def test_id(self):
        """test_id
        """
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq3.id, 3)

    def test_size(self):
        """test_size
        """
        self.assertEqual(self.sq2.size, 1)
        self.assertEqual(self.sq4.size, 2)

    def test_size_parameter_send(self):
        """test_size_parameter_send
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square("string")

    def test_size_value_error(self):
        """test_size_value_error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq = Square(-5)

    def test_x(self):
        """test_x
        """
        self.assertEqual(self.sq1.x, 0)
        self.assertEqual(self.sq3.x, 4)

    def test_x_type_error(self):
        """test_x_type_error
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq = Square(5, "string")

    def test_x_value_error(self):
        """test_x_value_error
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq = Square(5, -5)

    def test_y(self):
        """test_y
        """
        self.assertEqual(self.sq2.y, 0)
        self.assertEqual(self.sq4.y, 4)

    def test_y_type_error(self):
        """test_y_type_error
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq = Square(5, 5, "string")

    def test_y_value_error(self):
        """test_y_value_error
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq = Square(5, 5, -5)

    def test_area(self):
        """test_area
        """
        self.assertEqual(self.sq1.area(), 25)
        self.assertEqual(self.sq3.area(), 9)

    def test_str(self):
        """test_str
        """
        self.assertEqual(str(self.sq2), "[Square] (2) 5/0 - 1")
