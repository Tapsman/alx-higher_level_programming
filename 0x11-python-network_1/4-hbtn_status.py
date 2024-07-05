#!/usr/bin/python3
"""
This is a python script fetches the https://alx-intranet.hbtn.io/status
using the requests package.
"""
import requests


if __name__ == "__main__":
    read = requests.get("https://alx-intranet.hbtn.io/status")
    t = read.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(t), t))
