#!/usr/bin/python3
"""Module learn how to  Search and update in a file"""


def append_after(filename="", search_string="", new_string=""):
    """function to inserts a line of text to a file,
    after each line containing a specific string """
    cp_line = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cp_line.append(line)
            if search_string in line:
                cp_line.append(new_string)
    with open(filename, mode="w", encoding='utf-8') as f:
        for line in cp_line:
            f.write(line)
