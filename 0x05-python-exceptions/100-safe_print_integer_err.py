#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """A function that will print an integer with {:d}.format().

    If a ValueError message appears, a corresponding
    message is printed to the standard error

    Args: (int): integer to print.

    Returns:
        If a TypeError or ValueError occurs - False
        otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc()[1]), file=sys.stderr)
        return (False)
