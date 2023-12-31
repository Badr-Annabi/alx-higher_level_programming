#!/usr/bin/python3
"""
101-stats

this script reads the stdin line by line and computes metrices
"""
import sys


total_size = 0
status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        slice = line.split()
        if len(slice) >= 2:
            a = i
            if slice[-2] in status_code:
                status_code[slice[-2]] += 1
                i += 1
            try:
                total_size += int(slice[-1])
                if a == i:
                    i += 1
            except FileNotFoundError:
                if a == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(status_code.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
