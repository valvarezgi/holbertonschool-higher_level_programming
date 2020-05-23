#!/usr/bin/python3
""" Function that prints someones name
    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """say_my_name prints a name

    Args:
        first_name (str): first name to print
        last_name (str, optional): Last name to print. Defaults to "".

    Raises:
        TypeError: First name must be a string
        TypeError: Last name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
