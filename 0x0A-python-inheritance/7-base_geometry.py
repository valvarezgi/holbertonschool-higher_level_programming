#!/usr/bin/python3
""" BaseGeometry
"""


class BaseGeometry:
    """ class with a public attribute
    """

    def area(self):
        """area 

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator 

        Args:
            name (str): [description]
            value (int): [description]

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
