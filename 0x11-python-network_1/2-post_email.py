#!/usr/bin/python3
"""
This Python script takes in URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    new_val = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(new_val).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        r = response.read().decode('utf8')
    print(r)
