#!/usr/bin/python3
"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix is the matrix to be operated on and div is the divider"""
    for i in matrix:
        if isinstance(i, list) is False and not isinstance(i,
                int) and not isinstance(i, float):
            raise TypeError("matrix must be a matrix(list of lists)
                            of integers/float")
