#!/usr/bin/python3
"""Module to test class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry that validated integer and return area """
    def area(self):
        """ raises an Exception because is not finished """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates if value is integer """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
