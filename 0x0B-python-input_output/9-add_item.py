#!/usr/bin/python3
""" add_item
"""

import sys

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

try:
    list_json = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_json = []

argc = len(sys.argv)
for index in range(1, argc):
    list_json.append(sys.argv[index])
save_to_json_file(list_json, "add_item.json")
