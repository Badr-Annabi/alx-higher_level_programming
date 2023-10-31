#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i - 26) % 2 != 0:
        i = i - 32
    elif (i - 26) % 2 == 0:
        i = i
    print("{}".format(chr(i)),end="")
