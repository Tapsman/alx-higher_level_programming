#!/usr/bin/python3
"""
This is a python script that  is going to:
    - Take in the URL and is going to send a POST request to the passed URL
    - And it has to take the email as the parameter and will display
    - The body response
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
