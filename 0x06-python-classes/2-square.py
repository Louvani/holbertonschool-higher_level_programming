#!/usr/bin/python3
""" definition of a square class """


class Square:
    """ defines a square with a private instance attribute"""
    def __init__(self, size=0):
        """size: Square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
