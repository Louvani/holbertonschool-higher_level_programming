#!/usr/bin/python3
""" Roman to Integer module
"""


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
        }
    num = 0
    for idx, roman_num in enumerate(roman_string):
        if roman_num in roman_dict and idx + 1 < len(roman_string):
            if roman_dict[roman_num] >= roman_dict[roman_string[idx+1]]:
                num += roman_dict[roman_num]
            else:
                num -= roman_dict[roman_num]
        elif roman_num in roman_dict:
            num += roman_dict[roman_num]
    return num
