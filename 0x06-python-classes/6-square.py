#!/usr/bin/python3
""" definition of a square class """


class Square:
    """ defines a square with a private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """size: Square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for i in range(0, self.__position[1]):
                    print("")
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            is_int = True
            for i in value:
                if not isinstance(i, int) or i < 0:
                    is_int = False
                    break
            if is_int:
                self.__position = value
            else:
                raise TypeError("position must be a tuple \
                    of 2 positive integers")
