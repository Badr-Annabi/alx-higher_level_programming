#!/usr/bin/python3

"""
Define a function that checks if an object
is a class that inherited from,
the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if an object
    is a class that inherited from
    the specified class, and False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
