#!/bin/bash
#This script takes in a URL as an argument, sends a GET request to URL
curl -s "$1" -X GET -H "X-School-User-Id: 98"
