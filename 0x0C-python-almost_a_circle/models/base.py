#!/usr/bin/python3
"""
Module with the Base class for
the proyect "almost a circle".
"""
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        new_list = []
        with open(filename, mode='w', encoding='utf-8') as f:
            if not list_objs:
                f.write(json.dumps(new_list))
            else:
                for list_o in range(len(list_objs)):
                    new_list.append(list_objs[list_o].to_dictionary())
                f.write(    )

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            object_x = []
            return object_x
        object_x = json.loads(json_string)
        return object_x

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(12, 6)
        if cls.__name__ == "Square":
            dummy = cls(12)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        new_list = []
        if path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), mode='r') as f:
                temp = cls.from_json_string(json.load(f.read())
                for item in temp:
                    new_list.append(cls.create(**item))
            return new_list
        else:
            return new_list
