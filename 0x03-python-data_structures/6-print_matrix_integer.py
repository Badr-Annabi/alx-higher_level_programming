#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for line in matrix:
        if len(line) == 0:
            print()
        for i in range(len(line)):
            print("{}".format(line[i]),
                    end="\n" if i is len(line) - 1 else " ")
