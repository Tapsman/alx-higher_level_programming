#!/usr/bin/python3
"""
This is a python script that will take in a URL and send
a requests to the URL and then is going to display the value of the
variable X-Request-Id in the response header.
"""
import requests
import sys


url = sys.argv[1]

read = requests.get(url)
print(read.headers.get("X-Request-Id"))

if __name__ == "__main__":
