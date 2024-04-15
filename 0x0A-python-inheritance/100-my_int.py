#!/usr/bin/python3
"""
Containing the class MyInt
"""


class MyInt(int):
    """The rebel version of an integer, perfect for opposition day!"""
    def __new__cls, *args, **kwargs):
        """create a new instance of a class"""
        return super(MyInt, csl).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """What was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """What was == is now !="""
        return int(self) == other
