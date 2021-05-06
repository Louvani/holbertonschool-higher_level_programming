#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        dict1 = {key: value}
        a_dictionary.update(dict1)
    return a_dictionary
