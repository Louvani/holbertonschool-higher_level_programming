#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx + 1 > len(my_list):
        return None
    return my_list[idx]
