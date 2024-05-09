#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """The function divides all elements of the matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the div is not an int or a float.
        ZeroDivisionError: If the div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix msut be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of elements must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("dive must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
