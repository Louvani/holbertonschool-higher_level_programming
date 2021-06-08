#!/usr/bin/python3
"""
Module with the Base class for
the proyect "almost a circle".
"""
import json


class Base:
    """Base clase"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the id of the objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        print(filename)
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(list_objs))
