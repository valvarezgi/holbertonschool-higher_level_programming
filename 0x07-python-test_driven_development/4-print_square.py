#!/usr/bin/python3
""" Prints a square
"""


def print_square(size):
    """print_square

    Args:
        size (int): size of the square

    Raises:
        TypeError: size must be a an integer
        ValueError: size must be grater than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for idx in range(size):
            for idx2 in range(size):
                print("#", end="")
            print()
