#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = []
    for i in range(0, list_length):
        try:
            num.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            num.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            num.append(0)
            continue
        except IndexError:
            print("out of range")
            num.append(0)
    return num
