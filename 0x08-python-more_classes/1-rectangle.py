#!/usr/bin/python3
""""For rectangles"""


class Rectangle:
    """Class that define a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialice class Ractangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width only if is an integer and if is greather than 0"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self._height

    @height.setter
    def height(self, value):
        """set height only if is an integer and if is greather than 0"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
