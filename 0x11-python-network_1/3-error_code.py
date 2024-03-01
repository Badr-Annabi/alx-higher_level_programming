#!/usr/bin/python3
"""
This Python script sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:

            request = response.read().decode('utf8')
            print(request)

    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
