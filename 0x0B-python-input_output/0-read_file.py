#!/usr/bin/python3
""" [summary]
"""


def read_file(filename=""):
    """read_file

    Args:
        filename (str, optional): file name to open. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
