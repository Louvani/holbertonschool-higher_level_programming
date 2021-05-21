#!/usr/bin/python3
""""Help on class Rectangel in module 4-rectangle:"""


class Rectangle:
    """Class that define a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """return the rectangle with the character #"""
        new_string = ''
        if self.__width == 0 or self.__height == 0:
            return new_string
        for height in range(self.__height):
            for width in range(self.__width):
                new_string += str(self.print_symbol)
            if height < self.__height - 1:
                new_string += '\n'
        return new_string

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        new_string = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return new_string

    def __del__(self):
        """Called as soon as all references of the object are deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            area_1 = Rectangle.area(rect_1)
            area_2 = Rectangle.area(rect_2)
            if area_1 == area_2:
                return rect_1
            elif area_1 > area_2:
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)

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
        return self.__height

    @height.setter
    def height(self, value):
        """set height only if is an integer and if is greather than 0"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
