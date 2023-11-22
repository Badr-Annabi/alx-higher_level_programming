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
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2\
           or type(position[0]) is not int or type(position[1])\
           is not int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
        """
            Returning the position of the square

            Return:
                The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Sets the position of the square

            Args:
                None

            Return:
                None
        """
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1])\
           is not int or value[0] < 0 or value[1] < 0:
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
        """
        printing stdout the square using #

        Args:
            None
        Return:
            None
        """
        size = self.size
        position = self.position
        if size == 0:
            print()
        else:
            for i in range(position[1]):
                print()
            for i in range(size):
                print(" " * position[0] + "#" * size)

    def __str__(self):
        """
        Special method for Class Object strings
        """
        size = self.__size
        position = self.__position
        if size != 0:
            [print("") for i in range(position[1])]
        for i in range(size):
            [print(" ", end="") for j in range(0, position[0])]
            [print("#", end="") for k in range(0, size)]
            if i != size - 1:
                print("")
        return ""
