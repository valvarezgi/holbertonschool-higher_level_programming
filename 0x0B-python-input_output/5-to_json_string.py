#!/usr/bin/python3
""" to_json_string
"""
import json


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj: object to make the json representation

    Returns:
        str: json reprensentation of my_object
    """
    return json.dumps(my_obj)
