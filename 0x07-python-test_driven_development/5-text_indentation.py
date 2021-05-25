#!/usr/bin/python3
"""print new lines in texts"""


def text_indentation(text):
    """Print new lines when text have '.', '?', ':'"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        new_str = ""
        status = False  # for spaces at the begining of a line
        for idx, char in enumerate(text):
            if char == ' ' and new_str == "":
                continue
            if char == '.' or char == '?' or char == ':':
                new_str += char + '\n\n'
                status = True
            elif char is ' ' and status:
                continue
            else:
                status = False
                new_str += char
        new_str = new_str.splitlines(True)
        for line in new_str:
            print(line.strip(" "), end="")
