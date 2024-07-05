#!/usr/bin/python3
"""
This is a python script that will:
    - Take in the URL
    - Will send a request to the URL
    - And then displays the value of the X-Request-ID
    - Of the variable that is found on the header of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
