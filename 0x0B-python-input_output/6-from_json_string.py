#!/usr/bin/python3
""" from json to string
"""
import json


def from_json_string(my_str):
    """from_json_string

    Args:
        my_str (str): string to decode

    Returns:
        object : data structure reprensented by json string
    """
    return json.loads(my_str)
