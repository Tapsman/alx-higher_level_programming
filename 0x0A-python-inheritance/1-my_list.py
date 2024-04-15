#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """A class Mylist inherits from a list."""
    def print_sorted(self):
        """The method for printing the sorted list"""
        print(sorted(self))
