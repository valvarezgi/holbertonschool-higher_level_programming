#!/usr/bin/python3
""" number_of_lines
"""


def number_of_lines(filename=""):
    """number_of_lines

    Args:
        filename (str, optional): file name to count lines. Defaults to "".

    Returns:
        int: = number of lines
    """
    counter = 0
    with open(filename, "r") as f:
        for line in f:
            counter += 1
    return counter
