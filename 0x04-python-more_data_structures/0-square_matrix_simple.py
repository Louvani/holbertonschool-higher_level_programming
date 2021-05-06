#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda x: x ** 2, num)) for num in matrix]
    return new_matrix
