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
        else:
            return True


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers, validated
        by integer_validator
        """
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
