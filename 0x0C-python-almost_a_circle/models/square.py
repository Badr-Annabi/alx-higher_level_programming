#!/usr/bin/python3

""" This module defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return (
                "[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
