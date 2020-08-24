#!/usr/bin/python3
"""Searchs API"""
import requests
from sys import argv

if __name__ == "__main__":
    parameters = dict(q="")

    if len(argv) > 1:
        parameters['q'] = argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", parameters)
    try:
        response = req.json()
        if response:
            print('[{}] {}'.format(response.get('id'), body.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
