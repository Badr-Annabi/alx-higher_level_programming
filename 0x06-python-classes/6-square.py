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
    def __init__(self, size=0, position=(0, 0)):
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
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(
                value, tuple) or len(value) != 2 or not all(
                (isinstance(value[0], int) or isinstance(value[1], int)) or (
                    value[0] >= 0 or value[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculation and return the square's area.

        Return:
        the area.
        """
        return self.__size ** 2

    def my_print(self):

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
