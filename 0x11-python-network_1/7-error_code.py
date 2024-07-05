#!/usr/bin/python3
"""Takes in URL, sends requests to it, displays the body response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    read = requests.get(url)
    if read.stat_code >= 400:
        print("Error code: {}".format(read.stat_code))
    else:
        print(read.text)
