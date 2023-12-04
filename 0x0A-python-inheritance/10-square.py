#!/usr/bin/python3

"""Module that Defines a Square Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square which inherit from Rectangle"""

    def __init__(self, size):
        """
        Initialisation method
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area"""
        return (self.__size)**2

    def __str__(self):
        """Prints the Rectangle"""
        return ("[Rectangle]".format(self.__size))
