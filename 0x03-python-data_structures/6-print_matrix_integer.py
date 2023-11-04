#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for line in matrix:
        if len(line) == 0:
            print()
        for i in range(len(line)):
            seperator = "\n" if i is len(line) - 1 else " "
            print("{i:d}".format(line[i]), end=seperator)
