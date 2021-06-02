#!/usr/bin/python3
"""Module to test class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator('size', self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return area of a square"""
        return self.__size ** 2
