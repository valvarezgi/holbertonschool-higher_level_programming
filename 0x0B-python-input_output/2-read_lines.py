#!/usr/bin/python3
""" read_lines
"""


def read_lines(filename="", nb_lines=0):
    """read_lines

    Args:
        filename (str, optional): file to read. Defaults to "".
        nb_lines (int, optional): lines to read. Defaults to 0.
    """
    with open(filename, "r", encoding="utf-8") as f:
        counter = 0
        while nb_lines <= 0 or nb_lines > counter:
            line = f.readline()
            if not line:
                break
            counter += 1
            print(line, end="")
