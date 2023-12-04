#!/usr/bin/python3

"""
Define a Class that inherits from list.
"""


class MyList(list):
    """
    Inherits from list and provides a method to print
    the sorted list
    """

    def print_sorted(self):
        """Printd the list sortef in ascending order."""
        print(sorted(self))
