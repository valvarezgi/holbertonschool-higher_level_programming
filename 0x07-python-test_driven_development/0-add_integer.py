#!/usr/bin/python3
"""add_integer:
    Function that adds two integers
"""


def add_integer(a, b=98):
    """add_integer:
        Checks if 'a' and 'b' are integer or floats.
        If 'a' or 'b' are floats, cast to integers.
        Return sum of 'a' + 'b'.
    Args:
        a (int): First number to add
        b (int, optional): Second number to add. Defaults to 98.
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        if abs(a + b) == float('inf'):
            raise OverflowError("int too large to convert to float")
        return a + b
