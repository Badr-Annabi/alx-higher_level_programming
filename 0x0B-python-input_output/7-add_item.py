#!/usr/bin/python3
"""
Script that adds all arguments to
a Python list, and then save them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    filename = "add_item.json"

    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
