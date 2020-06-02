#!/usr/bin/python3
""" lookup
"""


def lookup(obj):
    """lookup

    Args:
        obj (any): any object

    Returns:
        list: list of available attributes and methods
            of an object
    """
    return dir(obj)
