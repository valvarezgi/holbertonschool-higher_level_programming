#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Defines Square Class.

    Square class with private attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ size

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Args:
            value (tuple): position

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is str or type(value[1]) is str:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method

        Area of the Square

        Returns:
            integer: square area
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method

        Prints a square in stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                for i in range(self.size):
                    print("#", end="")
                print()
