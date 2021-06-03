#!/usr/bin/python3
"""11. Student to disk and reload  """


class Student:
    """a class Student that defines a student by"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance (same as 8-class_to_json.py)"""
        if attrs is None:
            return vars(self)
        if all(isinstance(args, str) for args in attrs):
            new_dict = {}
            for args in attrs:
                if args in self.__dict__:
                    new_dict[args] = self.__dict__[args]
            return new_dict
        else:
            return vars(self)

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
