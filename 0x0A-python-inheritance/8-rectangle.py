#!/usr/bin/python3
"""Importing"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define a Rectangle module"""


class Rectangle(BaseGeometry):
    """Class that inherit from BaseGeometry Class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
