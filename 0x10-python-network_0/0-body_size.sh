#!/usr/bin/python3
# This is a bash script that takes a URL, sends a request
# to that URL and then displays the size of the body of
# the responces
curl -s "$1" | wc -c
