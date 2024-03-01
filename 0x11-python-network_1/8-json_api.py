#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    res = requests.get(url, payload)
    try:
        json_res = res.json()
        if json_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                json_res.['id'], json_res['name']))
    except ValueError:
        print("Not a valid JSON")
