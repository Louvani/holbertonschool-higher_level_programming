#!/usr/bin/python3
""""For rectangles"""


class Rectangle:
    """Class that define a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        new_string = ''
        if self.__width == 0 or self.__height == 0:
            return new_string
        for height in range(self.__height):
            for width in range(self.__width):
                new_string += '#'
            if height < self.__height - 1:
                new_string += '\n'
        return new_string

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
