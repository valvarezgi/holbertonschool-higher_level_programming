#!/usr/bin/python3
""" write_line
"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
