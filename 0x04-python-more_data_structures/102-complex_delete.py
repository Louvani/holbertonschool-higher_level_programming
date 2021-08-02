#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_remove = []
    for key, values in a_dictionary.items():
        if value == values:
            key_to_remove.append(key)
    for k in key_to_remove:
        del a_dictionary[k]
    return a_dictionary
