#!/usr/bin/python3

def matrix_divided(matrix, div):
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
