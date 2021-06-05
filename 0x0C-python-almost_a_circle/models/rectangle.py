#!/usr/bin/python3
"""First Rectangle """

from models.base import Base


class Rectangle(Base):
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class construcctor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # SETTER AND GETTER

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width only if is an integer and if is greather than 0"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
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
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    # METHODS

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        new_string = ''
        if self.__y > 0:
            print('\n' * (self.__y - 1))
        for height in range(self.__height):
            if self.__x > 0:
                new_string += ' ' * self.__x
            new_string += '#' * self.__width
            if height < self.__height - 1:
                new_string += '\n'
        print(new_string)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        new_string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
        self.__x, self.__y, self.__width, self.__height)
        return new_string
