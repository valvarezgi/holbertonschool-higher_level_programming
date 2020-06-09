#!/usr/bin/pyhon3
""" TestRectangle
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """Test_Rectangle [summary]

    Args:
        unittest ([type]): [description]
    """

    def setUp(self):
        """setUp
        """
        Base._Base__nb_objects = 0
        self.rec1 = Rectangle(10, 2)
        self.rec2 = Rectangle(2, 3, 2)
        self.rec3 = Rectangle(1, 2, 3, 4, 8)
        self.rec4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """test_id
        """
        self.assertEqual(self.rec1.id, 1)
        self.assertEqual(self.rec2.id, 2)
        self.assertEqual(self.rec3.id, 8)

    def test_width_parameter_send(self):
        """test_width_parameter_send
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_width(self):
        """test_width
        """
        self.assertEqual(self.rec1.width, 10)
        self.assertEqual(self.rec3.width, 1)

    def test_width_type_error(self):
        """test_width_type_error [summary]
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("string", 2)

    def test_width_value_error(self):
        """test_width_value_error [summary]
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-5, 5)

    def test_height_parameter_send(self):
        """test_height_parameter_send
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5)

    def test_height(self):
        """test_height
        """
        self.assertEqual(self.rec2.height, 3)
        self.assertEqual(self.rec4.height, 12)

    def test_height_type_error(self):
        """test_height_type_error
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, "string")

    def test_height_value_error(self):
        """test_height_value_error
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, -5)

    def test_x(self):
        """test_x
        """
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec3.x, 3)

    def test_x_type_error(self):
        """test_x_type_error
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(5, 5, "string")

    def test_x_value_error(self):
        """test_x_value_error
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(5, 5, -5)

    def test_y(self):
        """test_y
        """
        self.assertEqual(self.rec2.y, 0)
        self.assertEqual(self.rec4.y, 14)

    def test_y_type_error(self):
        """test_y_type_error
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(5, 5, 5, "string")

    def test_y_value_error(self):
        """test_y_value_error
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(5, 5, 5, -5)

    def test_area(self):
        """test_area
        """
        self.assertEqual(self.rec1.area(), 20)
        self.assertEqual(self.rec3.area(), 2)

    def test_str(self):
        """test_str
        """
        self.assertEqual(str(self.rec2), "[Rectangle] (2) 2/0 - 2/3")
        self.assertEqual(str(self.rec4), "[Rectangle] (3) 13/14 - 11/12")
