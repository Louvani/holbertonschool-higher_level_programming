#!/usr/bin/python3
'''function that returns the weighted average of all integers tuple
'''


def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    a = 0
    b = 0
    for score, weight in my_list:
        a += score * weight
        b += weight
    return a / b
