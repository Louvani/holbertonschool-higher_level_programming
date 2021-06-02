#!/usr/bin/python3
"""From JSON string to Object """

import json


def from_json_string(my_str):
    """Write a function that returns an object
    (Python data structure) represented by a JSON string"""
    object_x = json.loads(my_str)
    return object_x
