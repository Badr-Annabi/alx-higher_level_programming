#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = list.copy(my_list)
    if idx < 0 or idx >= len(my_list):
        return cp_list
    cp_list[idx] = element
    return cp_list
