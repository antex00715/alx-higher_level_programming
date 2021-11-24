#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return ([[i * i for i in row]) for row in matrix])
