#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # lenght of tuples
    a = len(tuple_a)
    b = len(tuple_b)
    # addition keep in variables
    n1 = (tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0)
    n2 = (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0)
    # put variables in a tuple
    add_tup = n1, n2
    return add_tup
