#!/usr/bin/python3
"""displays the body of a url response decoded in utf-8"""
from urllib import error, request
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode())
        except error.HTTPError as http_error:
            print('Error code: {}'.format(http_error.code))
