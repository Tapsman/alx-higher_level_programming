#!/usr/bin/python3
"""Script will take Github credentials and uses API to the id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    read = requests.get("https://api.github.com/user", auth=auth)
    print(read.json().get("id"))
