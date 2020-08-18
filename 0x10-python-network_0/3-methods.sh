#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -X -sI 'OPTIONS' "$1" | grep ALlow | cut -d " " -f2-
