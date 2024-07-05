#!/usr/bin/python3
"""Script will take URL, sends request and then displays body of response"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as er:
        print("Error code:", er.code)
