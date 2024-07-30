#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password),
and uses the GitHub API to display id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    github_user = sys.argv[1]
    pAt = sys.argv[2]
    req_auth = HTTPBasicAuth(github_user, pAt)
    try:
        resp = requests.get(url, auth=req_auth)
        print(resp.json().get("id"))
    except ValueError:
        print('None')
