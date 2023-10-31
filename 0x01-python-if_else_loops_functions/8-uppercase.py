#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            up = chr(ord(i) - ord('a') + ord('A'))
        else:
            up = i
        print("{}".format(up), end="")
    print()
