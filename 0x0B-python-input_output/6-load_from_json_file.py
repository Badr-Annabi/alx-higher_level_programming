#!/usr/bin/python3

"""
Define  a function
that  creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
     creates an Object from a “JSON file”
    """
    with open(filename, mode="r") as file:
        return json.load(file)
