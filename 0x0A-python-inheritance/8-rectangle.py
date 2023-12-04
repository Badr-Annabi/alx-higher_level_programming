#!/usr/bin/python3

"""Define an empty class"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Define a Rectangle module"""


class Rectangle(BaseGeometry):
    """Class that inherit from BaseGeometry Class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height


    