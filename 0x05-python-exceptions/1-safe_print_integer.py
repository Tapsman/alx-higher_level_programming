#!/usr/bin/python3

def safe_print_integer(value):
    """A function to print an integer with "{:d}.format.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
