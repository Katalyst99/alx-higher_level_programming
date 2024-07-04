#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
curl -s -o /dev/null "$1" '%{http_code}\n'
