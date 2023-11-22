#!/usr/bin/python3
"""
    MagicClass:

"""
import math


class MagicClass:
    """
    Initialisation of MagicClass
    """

    def __init__(self, radius=0):
        """
        Initialisation of our data

        Args:
            radius(type [int, float]): the radius of the MagicClass

        Return:
            None
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        All calculations for the area of the MagicClass
        """
        return self.__radius ** 2 * 2

    def circumference(self):
        """
        All calculations for circumference of the MagicClass
        """
        return 2 * math.pi * self.__radius
