#!/bin/bash
#!This Bash script sends a req to URL
curl -s -o /dev/null -w "%{http_code}" "$1"
