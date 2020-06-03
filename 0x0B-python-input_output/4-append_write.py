#!/usr/bin/python3
""" append_write
"""


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to append. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
