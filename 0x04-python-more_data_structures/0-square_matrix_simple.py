#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    if matrix is None:
        return None
    if not matrix:
        return None
    for lists in matrix:
        for num in lists:
            num **= 2
            squared.append(num)

    r_1 = squared[:3]
    r_2 = squared[3:6]
    r_3 = squared[-3:]
    column = []
    column.append(r_1)
    column.append(r_2)
    column.append(r_3)
    return column
