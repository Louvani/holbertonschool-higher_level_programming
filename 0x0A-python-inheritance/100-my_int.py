#!/usr/bin/python3
"""module to create My integer """


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, x):
        if int(self) == int(x):
            return False
        else:
            return True

    def __ne__(self, x):
        if int(self) != int(x):
            return False
        else:
            return True
