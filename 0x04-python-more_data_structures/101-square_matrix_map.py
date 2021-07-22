#!/usr/bin/python3
'''
function that computes the square value
of all integers of a matrix using map
'''


def square_matrix_map(matrix=[]):
    new = list(map(lambda i: list(map(lambda item: item ** 2, i)), matrix))
    return new
