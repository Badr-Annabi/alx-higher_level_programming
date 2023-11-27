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
    number_of_instances = 0
    print_symbol = "#"

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
            Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Print a rectangle using the character #
        """
        if (self.__width or self.__height) == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width + '\n'
        return result.rstrip('\n')

    def __repr__(self):
        """
        Return a string representation
        """
        return "Rectangle(2, 4)".format(self.__width, self.__height)

    def __del__(self):
        """Prints Bye rectangle when it deletes it """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
