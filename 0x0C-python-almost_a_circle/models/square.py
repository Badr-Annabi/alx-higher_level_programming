#!/usr/bin/python3

""" This module defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ This module defines a Square Class"""
        return self.width

    @size.setter
    def size(self, value):
        """ This module defines a Square Class"""
        self.width = value
        self.height = value

    def __str__(self):
        """ This module defines a Square Class"""
        return (
                "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ This module defines a Square Class"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """ This module defines a Square Class"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
