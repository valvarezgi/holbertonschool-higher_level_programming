#!/usr/bin/python3
""" Class Student
"""


class Student:
    """ Class Student
    """

    def __init__(self, first_name, last_name, age):
        """__init__

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json

        Returns:
            [type]: [description]
        """
        if attrs is not None:
            dictionary = {}
            for key_1, value in self.__dict__.items():
                for key_2 in attrs:
                    if key_1 == key_2:
                        dictionary.update({key_1: value})
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json

        Args:
            json ([type]): [description]
        """
        for key, value in json.items():
            self.__dict__[key] = value
