#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as respon:
        hTmL = respon.read()
        print("Body response:")
        print('\t- type: {}'.format(type(hTmL)))
        print("\t- content: {}".format(hTmL))
        print("\t- utf8 content: {}".format(hTmL.decode('utf8')))
