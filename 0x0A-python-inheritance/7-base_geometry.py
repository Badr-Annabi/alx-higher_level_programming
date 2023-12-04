#!/usr/bin/python3

"""Define an empty class"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            checks value and raises errors
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
