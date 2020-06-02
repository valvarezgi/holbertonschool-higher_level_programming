#!/usr/bin/python3
""" inherits_from
"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj (object): object to evaluate
        a_class (class):  class to evaluate
    """
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
