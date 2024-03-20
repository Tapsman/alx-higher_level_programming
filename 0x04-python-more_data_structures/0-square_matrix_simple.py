#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    recent_matrix = matrix.copy()

    for i in range(len(matrix)):
        recent_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (recent_matrix)
