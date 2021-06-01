#!/usr/bin/python3
"""Module to check the instance of a object."""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
    of the specified class ; otherwise False."""

    t_string = type(obj)
    return (True if t_string == a_class else False)
