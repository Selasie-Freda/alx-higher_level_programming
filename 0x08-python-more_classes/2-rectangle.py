#!/usr/bin/python3
""" a class Rectangle that defines a rectangle"""


class Rectangle:
    """defines area and perimeter attributes"""

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be )= 0")
            else:
                self.__height = value

        def area(self):
            return self.__width * self.__height

        def perimeter(self):
            if self.__height == 0 or self.__width == 0:
                return 0
            else:
                return 2 * (self.__height + self.__width)
