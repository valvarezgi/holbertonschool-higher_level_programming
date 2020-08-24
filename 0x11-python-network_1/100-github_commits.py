#!/usr/bin/python3
"""List 10 commits"""
import requests
from sys import argv

if __name__ == "__main__":
    Link = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    ReqData = requests.get(Link)
    commits = ReqData.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
