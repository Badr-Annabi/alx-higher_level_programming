#!/bin/bash
#This script takes in a URL as an argument, sends a Post request to URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
