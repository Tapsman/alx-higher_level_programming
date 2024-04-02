#!/usr/bin/python3
"""Program to Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """It now returns the current area of the square"""
        return (self.__size * self.__size)
