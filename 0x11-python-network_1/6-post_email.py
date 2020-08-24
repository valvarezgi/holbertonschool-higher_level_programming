#!/usr/bin/python3
"""displays the response of send POST request to an URL"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.post(argv[1], dict(email=argv[2]))
    print(req.text)
