#!/usr/bin/python3
"""Doc for subclass topic"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class; otherwise False."""

    type_string = type(obj)
    if type_string == a_class:
        return False
    return (True if issubclass(type_string, a_class) else False)
