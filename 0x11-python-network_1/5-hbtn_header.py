#!/usr/bin/python3
"""
This Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argc[1]
    res = requests.get(url)
    request_id = res.header.get('X-Request-Id')
    print(request_id)
