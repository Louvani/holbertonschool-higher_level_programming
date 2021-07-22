#!/usr/bin/python3
"""Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """
    triangle = []
    if n <= 0:
        return triangle
    for row in range(1, n + 1):
        lines = []
        num = 1
        for column in range(1, row + 1):
            lines.append(num)
            num = round(num * (row - column) / column)
        triangle.append(lines)
    return triangle
