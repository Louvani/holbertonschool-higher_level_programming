#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for n in range(len(my_list)):
        if my_list[n] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[n])
    return new_list
