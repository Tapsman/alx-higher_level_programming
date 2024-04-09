#!/usr/bin/python3
"""The class defines a locked class."""


class LockedClass:
    """

    Prevent the user from instantiating a new LockedClass attributes
    for anything but attributes called 'first_name.'
    """

    __slots__ = ["first_name"]
