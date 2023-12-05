#!/usr/bin/python3

"""Function that Appends into a text file"""


def append_write(filename="", text=""):
    """Appends into a text file (UTF8)
    and returns the number of characters
    written"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
