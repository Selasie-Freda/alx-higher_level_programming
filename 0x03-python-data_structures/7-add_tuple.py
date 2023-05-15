#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_list = list(tuple_a)
    tuple_b_list = list(tuple_b)

    while len(tuple_a_list) < 2:
        tuple_a_list.append(0)
    while len(tuple_b_list) < 2:
        tuple_b_list.append(0)
    new_tuple = ((tuple_a_list[0] + tuple_b_list[0]), (tuple_a_list[1] + tuple_b_list[1]))
    return new_tuple
