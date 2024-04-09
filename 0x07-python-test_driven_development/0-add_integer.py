#!/usr/bin/python3
"""A function that defines an integer addition"""


def add_integer(a, b=98):
    """Function to return the addition of integers a and b.

    Float arguments are typecasted to ints before the additions are formed.


    Raises:
        TypeError: if either a or b is non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
