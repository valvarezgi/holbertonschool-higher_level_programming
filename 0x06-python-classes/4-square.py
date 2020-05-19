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
        self.size = size

    @property
    def size(self):
        """size getter

        Returns:
            integer: size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value (integer): size of the Square

        Raises:
            TypeError: Value different from integer
            ValueError: Value less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area method

        Area of the Square

        Returns:
            integer: square area
        """
        return self.__size * self.__size
