#!/usr/bin/python3
"""
This Python script takes 2 arguments in order to solve this challenge.
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/{}/{}/commits/".format(
            sys.argv[2], sys.argv[1])
    res = requests.get(url)
    commit = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
