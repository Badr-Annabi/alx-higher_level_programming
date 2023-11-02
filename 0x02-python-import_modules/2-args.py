#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    elems = len(sys.argv) - 1
    if elems == 0:
        print("0 arguments.")
    elif elems == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(elems))
    for i in range(elems):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
