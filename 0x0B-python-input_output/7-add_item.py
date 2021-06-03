#!/usr/bin/python3
""" 7. Load, add, save """

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    variable_x = load_from_json_file("add_item.json")
except:
    variable_x = []

for argumentos in range(1, len(argv)):
    variable_x.append(argv[argumentos])

save_to_json_file(variable_x, "add_item.json")
