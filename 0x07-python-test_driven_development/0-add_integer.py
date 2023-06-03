#!/usr/bin/python3
"""
0-add_integer.py
"""


def add_integer(a, b=98):
    """function that adds 2 integers. It accepts only integers or floats
    a TypeError is raised when argument passed is not float or intger"""
    if type(a) != int and type(a) != float and type(
            b) != int and type(b) != float:
        raise TypeError("a and b must be integers")
    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if isinstance(a, int) is True and isinstance(b, int) is True:
        ans = a + b
        return ans
