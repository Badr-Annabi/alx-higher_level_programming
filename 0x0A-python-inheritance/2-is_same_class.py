#!/usr/bin/python3

"""
Define a function that checks if an object
is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if an object
    is an instance of a specific class, and
    False otherwise
    """
    return type(obj) is a_class
