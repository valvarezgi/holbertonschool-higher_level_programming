#!/usr/bin/python3
"""desplays value of the X-Request-Id header"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
