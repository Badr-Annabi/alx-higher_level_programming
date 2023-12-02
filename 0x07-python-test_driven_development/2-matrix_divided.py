#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div equals to 0.

    Returns:
        A new matrix representing the result of the division.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists)of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    result = []
    for submatrix in matrix:
        if not isinstance(submatrix, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        else:
            leng = len(matrix[0])
        if not (len(submatrix) == leng):
            raise TypeError("Each row of the matrix must "
                            "have the same size")
        for i in submatrix:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            result.append(round(i / div, 2))
        new_matrix.append(result)
        result = []
    return new_matrix
