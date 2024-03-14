#!/usr/bin/python3
if __name__ == "__main__":
    """Program to print addition of all the arguments"""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total = total + int(sys.argv[i + 1])
    print("{}".format(total))
