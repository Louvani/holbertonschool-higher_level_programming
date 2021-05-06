#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in matrix[i]]for i in range(len(matrix))]
    return new_matrix
