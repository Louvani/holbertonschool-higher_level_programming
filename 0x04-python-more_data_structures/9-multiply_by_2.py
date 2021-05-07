#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    new_d = list(a_dictionary)
    for k in new_d:
        new_dictionary[k] = a_dictionary[k] * 2
    return new_dictionary
