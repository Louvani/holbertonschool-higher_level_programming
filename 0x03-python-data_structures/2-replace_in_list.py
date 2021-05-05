#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx + 1 > len(my_list):
        return None
    my_list[idx] = element
    return my_list
