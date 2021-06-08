#!/usr/bin/python3
"""10. And now, the Square! """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class construcctor"""
        super().__init__(size, size, x, y, id)

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

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        new_string = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
        return new_string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            list_args = ['id', 'size', 'x', 'y']
            for value in range(len(args)):
                setattr(self, list_args[value], args[value])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        new_dict = {}
        list_args = ['id', 'size', 'x', 'y']
        for key in list_args:
            if key == 'size':
                new_dict[key] = self.__dict__['_Rectangle__width']
            elif key == 'id':
                new_dict[key] = self.__dict__[key]
            else:
                new_dict[key] = self.__dict__['_Rectangle__' + key]
        return new_dict
