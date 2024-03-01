#!/usr/bin/python3
"""
This python script displays the value of
the X-Request-Id var in the header
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id", None)
        if x_request_id:
            print(x_request_id)
