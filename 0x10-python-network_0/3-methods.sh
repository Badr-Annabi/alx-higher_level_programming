#!/bin/bash
#This script that takes in URL and displays all HTTP method.
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
