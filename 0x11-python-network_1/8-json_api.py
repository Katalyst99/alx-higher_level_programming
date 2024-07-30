#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to http://0.0.0.0:5000/search_user,
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letr = {}
    if len(sys.argv) > 1:
        letr["q"] = sys.argv[1]
    else:
        letr["q"] = ""

    resp = requests.post(url, letr)

    try:
        j_dict = resp.json()
        if j_dict:
            print('[{}] {}'.format(j_dict.get('id'), j_dict.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
