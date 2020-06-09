#!/usr/bin/python3
""" class Base
"""

import json
import unittest


class Base:
    """ Class Base, private attribute __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ constructor

        Args:
            id (int, optional): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string

        Args:
            list_dictionaries : list dictionaries

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Args:
            list_objs ([type])
        """
        list_to_print = []
        if list_objs is not None:
            for idx in list_objs:
                list_to_print.append(idx.to_dictionary())

        with open("{}.json".format(cls.__name__), "w", encoding="UTF8") as f:
            f.write(cls.to_json_string(list_to_print))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create [summary]

        Returns:
            [type]: [description]
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file [summary]

        Returns:
            [type]: [description]
        """
        to_print = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                files = cls.from_json_string(f.read())
                for fi in files:
                    to_print.append(cls.create(**fi))
        except:
            pass
        return to_print
