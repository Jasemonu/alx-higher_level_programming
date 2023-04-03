#!/usr/bin/python3
"""Defining class of a rectangle"""


class Rectangle:
    """"Initializing the class"""
    def __init__(self, width=0, height=0):
        """Args:
               Width: with of the rectangle
               height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """"width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns parametre of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width)*2

    def __str__(self):
        """returns a string with a special character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rect_str = ''
        for m in range(self.__height):
            for n in range(self.__width):
                rect_str += '#'
            if m < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message about a deleted object"""
        print("Bye rectangle...")
