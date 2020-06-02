#!/usr/bin/python3
""" is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Args:
        obj (object): object to evaluate
        a_class (class): class to evaluate
    """
    return(isinstance(obj, a_class))
