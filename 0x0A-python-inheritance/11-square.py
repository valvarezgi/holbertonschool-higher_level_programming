#!/usr/bin/python3
""" Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square [summary]

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size):
        """__init__ [summary]

        Args:
            size ([type]): [description]
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """__str__ [summary]
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
