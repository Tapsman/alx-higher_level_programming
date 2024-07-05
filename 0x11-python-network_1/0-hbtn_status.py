#!/usr/bin/python3
"""
- This is a python script that is going to fetch a
- https://alx-intranet.hbtn.io/status
- It then uses a with statement
- Using the urlib package
"""


if __name__ == "__main__":
    import urlib.request

    with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body responce:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
