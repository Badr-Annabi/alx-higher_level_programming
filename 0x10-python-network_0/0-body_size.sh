#!/bin/bash
#!This Bash script takes in a URL, sends a req to that URL and displays
#the size of the body of the res

curl -sI "$1" | awk '/Content-Length/ {print $2}'
