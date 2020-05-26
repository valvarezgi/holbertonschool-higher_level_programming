#!/usr/bin/python3
""" Defines a rectangle
"""


class Rectangle:
    """ Class to define a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ constructor

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """__str__

        Returns:
            str: prints the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        to_ptint = []
        for element in range(self.height):
            to_ptint.append("{}".format(self.print_symbol) * self.width)
            if element < self.height - 1:
                to_ptint.append("\n")
        return "".join(to_ptint)

    def __repr__(self):
        """__repr__

        Returns:
            str: string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """__del__ deletes an instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal

        Args:
            rect_1 (): [description]
            rect_2 (): [description]

        Raises:
            TypeError: [description]
            TypeError: [description]

        Returns:
            [type]: [description]
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2

    @classmethod
    def square(cls, size=0):
        """square [summary]

        Args:
            size (int, optional): . Defaults to 0.

        Returns:
            [type]:
        """
        return cls(size, size)
