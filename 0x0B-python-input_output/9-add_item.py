#!/usr/bin/python3

from sys import argv

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

list_json = []

try:
    list_json = load_from_json_file("add_item.json")
    for i in list_json:
        list_json.append(i)

except:
    pass

for i in range(len(argv)):
    if i != 0:
        list_json.append(argv[i])

save_to_json_file(list_json, "add_item.json")
