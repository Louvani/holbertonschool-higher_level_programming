#!/usr/bin/python3
"""Module to test class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers, validated
        by integer_validator
        """
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
