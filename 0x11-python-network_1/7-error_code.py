#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    # try:
    resp = requests.get(url)
    # except requests.exceptions.HTTPError as resp:
    if resp.status_code != 200:
        print('Error code: {}'.format(resp.status_code))
    else:
        print(resp.text)
