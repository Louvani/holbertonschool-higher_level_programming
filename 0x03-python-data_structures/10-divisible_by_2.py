#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_false = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            true_false.insert(i, True)
        else:
            true_false.insert(i, False)
    return true_false
