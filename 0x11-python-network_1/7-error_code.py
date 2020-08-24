#!/usr/bin/python3
"""send request to an URL and displays the body response"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
