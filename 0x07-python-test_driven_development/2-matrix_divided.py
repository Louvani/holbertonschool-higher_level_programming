#!/usr/bin/python3
"""Module that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all element of a matrix"""
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    if all(not isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    else:
        new_matrix = []
        for idx in range(len(matrix)):
            num_list = []
            temp = 0
            for num in range(len(matrix[idx])):
                if isinstance(matrix[idx][num], (int, float)):
                    num_list.append(round(matrix[idx][num] / div, 2))
                else:
                    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            new_matrix.append(num_list)
        return new_matrix
