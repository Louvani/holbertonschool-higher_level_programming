#!/usr/bin/python3
"""Doc for module 101"""


def add_attribute(obj, variable, value):

    type_str = type(obj)
    if "__dict__" in dir(type_str):
        setattr(obj, variable, value)
    else:
        raise TypeError("can't add new attribute")
