#!/usr/bin/python3
"""My Github"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(argv[1])
    req = requests.get(
        url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get("id"))
