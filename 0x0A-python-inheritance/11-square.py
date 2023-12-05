#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""Module Defines Square Class"""


class Square(Rectangle):
    """Class that defines a square and inherit from rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area"""
        return super().area()

    def __str__(self):
        """printing square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
