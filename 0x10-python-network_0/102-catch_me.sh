#!/bin/bash
#This Bash script sends a req to 0.0.0.0:5000/catch_me
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin" "Origin: HolbertonSchool"
