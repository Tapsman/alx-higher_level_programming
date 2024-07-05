#!/usr/bin/python3
"""
This is a python script that will take in a URL
and an email address
Then sends a POST request to the passed URL
with the email as its parameter
Then displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    read = requests.post(url, data=value)
    print(read.text)
