#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_d = sorted(list(a_dictionary))
    for k in new_d:
        value = a_dictionary[k]
        print("{}: {}".format(k, value))
