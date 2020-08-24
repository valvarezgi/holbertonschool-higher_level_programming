#!/usr/bin/python3
"""fetches an status"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format
              (type(the_page), the_page, the_page.decode('utf-8')))
