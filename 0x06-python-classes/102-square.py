#!/usr/bin/python3
"""
Module Name: square_module

This module defines a simple Square class.

Class:
    Square: Defines a square.

Atrribute:
    None
Usage:
    new_square = Square(n)

"""


class Square:
    """
    Initializes a new instance of square class.


    Args:
        __size (int): The size of the square.

        Return:
            None
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculation and return the square's area.

        Return:
        the area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NoImplemented
        return self.area() >= other.area()
