#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Defines Square Class.

    Square class with private attribute size
    """
    def __init__(self, size=0):
        """__init__ size

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
