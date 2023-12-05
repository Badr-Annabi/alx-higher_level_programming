#!/usr/bin/python3

"""
Module that defines MyInt
"""


class MyInt(int):
    """
    Class that inherit from int
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
