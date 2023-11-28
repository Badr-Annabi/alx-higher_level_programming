#!/usr/bin/python3

"""
Module Name: LockedClass.

This module (Class) prevents the user
from dynamically creating new
instance attributes, except if the
new instance attribute is called
first_name..

Class:
    LockedClass.

Atrribute:
    slots
Usage:
    LockedClass()
"""


class LockedClass:

    """
    A class that defines a rectangle

    Attribute:
    slots: defines a tuple of
    allowed attribute names

    Methods:
    None
    """

    __slots__ = ['first_name']
