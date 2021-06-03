#!/usr/bin/python3
""" 6. Create object from a JSON file """

import json


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        object_x = json.load(f)
    return object_x
