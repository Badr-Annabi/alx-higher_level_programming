#!/usr/bin/python3
""" This python script fetches the status from ALX intranet """


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print(f"    - type: {type(html)}")
    print(f"    - content: {html}")
    print(f"    - utf8 content: {html.decode('utf-8')}")
