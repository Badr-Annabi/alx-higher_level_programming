#!/bin/bash
#This Bash script sends a req to 0.0.0.0:5000/catch_me so it causes to respond a message "You got me!"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
