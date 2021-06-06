#!/usr/bin/python3
"""10. And now, the Square! """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        new_string = "[Square] ({}) {}/{} - {}/{}".format(self.id,
        self.x , self.y, self.width, self.height)
        return new_string

