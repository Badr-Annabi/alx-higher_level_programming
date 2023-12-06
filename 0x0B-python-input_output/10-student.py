#!/usr/bin/python3

"""Module that defines a student"""


class Student:
    """
    Class that defines a student by:

    Attributes: first_name, last_name, age.

    Methods: __init__. to_json.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__
        else:
            fill_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    fill_dict[attr] = getattr(self, attr)
            return fill_dict
