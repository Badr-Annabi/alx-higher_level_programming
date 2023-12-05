#!/usr/bin/python3

import json
"""
Define  a function
that returns the JSON representation
of an object (string):
"""


def to_json_string(my_obj):
    """
    Define  a function
    that returns the JSON representation
    of an object (string):
    """
    json_string = json.dumps(my_obj)
    return json_string
