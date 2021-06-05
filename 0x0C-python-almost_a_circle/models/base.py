#!/usr/bin/python3
"""
Module with the Base class for
the proyect "almost a circle".
"""


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
