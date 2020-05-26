#!/usr/bin/python3
""" Defines a rectangle
"""


class Rectangle:
    """ Class to define a rectangle
    """
    def __init__(self, width=0, height=0):
        """__init__ constructor

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            integer: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (integer): width of rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be grater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height setter

        Returns:
            integer: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (integer): height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be grater than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area

        Returns:
            integer: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter

        Returns:
            integer: perimeter of the rectangle
            if width or height are 0, then perimeter is zero
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
