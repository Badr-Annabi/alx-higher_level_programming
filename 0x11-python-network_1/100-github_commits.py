#!/usr/bin/python3
"""
This Python script takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(
            "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[2], sys.argv[1]))
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
