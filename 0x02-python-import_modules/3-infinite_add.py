#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    s = 0
    for i in range(args):
        s = s + int(sys.argv[i + 1])
    print("{}".format(s))
