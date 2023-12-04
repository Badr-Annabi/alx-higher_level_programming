#!/usr/bin/python3
"""
    Module for BaseGeometry Class and Rectangle Class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a Rectangle module"""


class Rectangle(BaseGeometry):
    """Class that inherit from BaseGeometry Class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
