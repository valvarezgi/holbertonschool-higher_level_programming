#!/usr/bin/python3
""" Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle [summary]

    Args:
        BaseGeometry ([type]): [description]
    """

    def __init__(self, width, height):
        """__init__ [summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
