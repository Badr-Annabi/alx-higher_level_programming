#!/usr/bin/python3

"""
Module Name: square_module

This module defines a simple rectangle class.

Class:
    rectangle: Defines a rectangle.

Atrribute:
    None
Usage:
    Rectangle()
"""


class Rectangle:
    """
    A class that defines a rectangle

    Attribute:
    width: Width of the rectangle.
    height: Height of the rectangle.

    Methods:
    def __init__(self, width=0, height=0)
    def width(self)
    def height(self)
    """

    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        This method returns a rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method returns a rectangle perimeter.
        """
        if (self.__width and self.__height) == 0:
            return 0
        return 2 * (self.__height + self.__width)
