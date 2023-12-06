#!/usr/bin/python3

"""reads stdin line by line and computes metrics."""
import sys


total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        slice = line.split()
        if len(slice) >= 2:
            j = i
            if slice[-2] in status_codes:
                status_codes[slice[-2]] += 1
                i += 1
            try:
                total_size += int(slice[-1])
                if j == i:
                    i += 1
            except FileNotFoundError:
                if j == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
