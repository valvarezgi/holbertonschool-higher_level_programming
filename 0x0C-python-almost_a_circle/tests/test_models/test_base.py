#!/usr/bin/python
""" TestBase
"""

import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase [summary]

    Args:
        unittest ([type]): [description]
    """
    def test_many_arguments(self):
        """test_many_arguments
        """
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_set_id(self):
        """test_set_id
        """
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_id(self):
        """test_id
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_zero(self):
        """test_zero [summary]
        """
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative(self):
        """test_negative [summary]
        """
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_float(self):
        """test_float
        """
        b = Base(2.5)
        self.assertEqual(b.id, 2.5)

    def test_string(self):
        """test_string
        """
        b = Base("String")
        self.assertEqual(b.id, "String")

    def test_nb(self):
        """test_nb
        """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__no_objects)

    def test_to_json_string(self):
        """test_to_json_string [summary]
        """
        Base._Base__nb_objects = 0
        dict1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        dict2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_string = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(json_string) is str)
        dict = json.loads(json_string)
        self.assertEqual(dict, [dict1, dict2])

    def test_None_to_json(self):
        """test_None_to_json
        """
        json_string = Base.to_json_string(None)
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_empty_from_json(self):
        """test_empty_from_json [summary]
        """
        self.assertEqual("[]", Base.from_json_string(""))
