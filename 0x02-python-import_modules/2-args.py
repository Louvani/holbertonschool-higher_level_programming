#!/usr/bin/python3
from sys import argv
lenght = len(argv)
print("0 arguments." if lenght == 1 else "{} arguments:".format(lenght - 1))
for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
