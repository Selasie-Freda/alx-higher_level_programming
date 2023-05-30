#!usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """nstantiation with optional size: def __init__(self, size=0):"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an int")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        Area = self.__size ** 2
        return Area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
