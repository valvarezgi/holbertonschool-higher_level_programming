#!/usr/bin/python3
"""POST an email and display the body of the response"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":

    url = argv[1]
    post_email = {'email': argv[2]}
    email = parse.urlencode(post_email)
    email = email.encode("utf-8")
    req = request.Request(url, email)

    with request.urlopen(req) as response:
        email_req = response.read()
        print(email_req.decode("utf-8"))
