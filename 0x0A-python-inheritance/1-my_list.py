#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        if len(self) == 0:
            print('[]')
        else:
            print(sorted(self))
