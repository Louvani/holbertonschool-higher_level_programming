#!/usr/bin/python3
"""10. And now, the Square! """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class construcctor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        new_string = "[Square] ({}) {}/{} - {}/{}".format(self.id,
        self.x , self.y, self.width, self.height)
        return new_string

    @property
    def size(self):
        """retrieve width"""
        return self.width

    @size.setter
    def size(self, value):
        """set width only if is an integer and if is greather than 0"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value
