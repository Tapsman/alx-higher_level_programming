#!/usr/bin/python3
"""
This is a python script that is going to:
    - Takes in a letter
    - Then sends a POST request to http://0.0.0.0:5000/search_user
    - The letter has to be a parameter
"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1:
        loader = {"q": letter}
    else:
        sys.argv[1]
        loader = {"q": letter}

    read = requests.post("http://0.0.0.0:5000/search_user", data=loader)
    try:
        res = read.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
