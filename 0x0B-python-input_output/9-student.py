#!/usr/bin/python3
"""9. Student to JSON """


class Student:
    """a class Student that defines a student by"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        of a Student instance (same as 8-class_to_json.py)"""
        return vars(self)
