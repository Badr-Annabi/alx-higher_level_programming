#!/bin/bash
#!This Bash script takes in a URL, sends a req to that URL
curl -sI "$1" | awk '/Content-Length/ {print $2}'
