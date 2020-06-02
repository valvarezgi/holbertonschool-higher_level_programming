#!/usr/bin/python3
""" MyList
"""


class MyList(list):
    """MyList

    Args:
        list (class): Inherits from list
    """

    def print_sorted(self):
        """print_sorted sorted a given list
        """
        print sorted(self)
