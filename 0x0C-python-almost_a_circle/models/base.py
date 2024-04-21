#!/usr/bin/python3
"""Module for Base Class"""


class Base:
    """A representation of the base of my OOP hierachy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
