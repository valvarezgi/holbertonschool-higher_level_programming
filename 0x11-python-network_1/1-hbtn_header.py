#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()
        print("{}".format(header.get("X-Request-Id")))
