#!/usr/bin/python3
""" save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Args:
        my_obj : object to write
        filename (str): name of the file to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
