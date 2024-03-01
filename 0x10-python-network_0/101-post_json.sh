#!/bin/bash
#This Bash script sends a req to 0.0.0.0:5000/catch_me
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
