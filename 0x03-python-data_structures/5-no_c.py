#!/usr/bin/python3
def no_c(my_string):
    count_c = my_string.count('c')
    my_string = list(my_string)
    while my_string.count('c') > 0:
        my_string.remove('c')
    my_string = "".join(my_string)
    my_string = list(my_string)
    while my_string.count('C') > 0:
        my_string.remove('C')
    my_string = "".join(my_string)
    return my_string
