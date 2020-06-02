#!/usr/bin/python3
""" is_same_class
"""


def is_same_class(obj, a_class):
    """is_same_class

    Args:
        obj (object): object to evaluate
        a_class (class): class

    Returns:
        Bool: True is the object is exactly an istance of the
        a_class
    """
    return type(obj) is a_class