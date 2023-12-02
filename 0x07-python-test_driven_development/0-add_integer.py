#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
     Adds two numbers and returns their sum.

    Parameters:
        a (int/float): The first number.
        b (int/float): The second number. Default to 98.

    Raises:
        TypeError

    Returns:
        int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
