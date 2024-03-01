#!/usr/bin/python3
""" This Python script fetches https://alx-intranet.hbtn.io/status """


import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    body = res.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
