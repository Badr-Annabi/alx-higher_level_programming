#!/usr/bin/python3
"""
This Python script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":

    res = requests.get('https://api.github.com/user', auth=(
        sys.argv[1], sys.argv[2]))
    json_res = res.json()
    try:
        print(json_res['id'])
