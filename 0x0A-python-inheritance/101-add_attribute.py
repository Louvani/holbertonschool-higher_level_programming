#!/usr/bin/python3
"""Doc for module 101 add atributte"""


def add_attribute(obj, variable, value):
    """function that adds a new attribute to an object if it’s possible"""
    type_str = type(obj)
    if "__dict__" in dir(type_str):
        setattr(obj, variable, value)
    else:
        raise TypeError("can't add new attribute")
