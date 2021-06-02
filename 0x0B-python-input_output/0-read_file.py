#!/usr/bin/python3
"""Module learn how to read a file"""


def read_file(filename=""):
    """function to read a file and write in the standar output"""
    with open(filename, encoding='utf-8') as f:
        print(f.read())
