#!/usr/bin/python3
"""Module to learn how to write a fille"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        number = f.write(text)
        return number
