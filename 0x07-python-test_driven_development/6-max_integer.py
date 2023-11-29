#!/usr/bin/python3
"""
Module that finds the max in a list of integers
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer
    """
    if len(list) == 0:
        return None
    max = list[0]
    i = 1
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
