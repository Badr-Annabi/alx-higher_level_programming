#!/usr/bin/python3

"""
Module that adds a new attribute
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object"""
    if "__dict__" in dir(obj):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
