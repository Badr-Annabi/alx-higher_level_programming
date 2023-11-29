#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        A new matrix represents the multiplication of m_a by m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for matrix, matrix_name in zip([m_a, m_b], ["m_a", "m_b"]):
        for List in matrix:
            if not isinstance(List, list):
                raise TypeError(matrix_name + " must be a list of lists")

    for matrix, matrix_name in zip([m_a, m_b], ["m_a", "m_b"]):
        if len(matrix) == 0:
            raise ValueError(matrix_name + " can't be empty")
        for List in matrix:
            if len(List) == 0:
                raise ValueError(matrix_name + " can't be empty")

    for matrix, matrix_name in zip([m_a, m_b], ["m_a", "m_b"]):
        for List in matrix:
            for n in List:
                if not isinstance(n, (int, float)):
                    raise TypeError(matrix_name + " should contain \
only integers or floats")

    for matrix, matrix_name in zip([m_a, m_b], ["m_a", "m_b"]):
        tmp_len = len(matrix[0])
        for List in matrix:
            if len(List) != tmp_len:
                raise TypeError("each row of " + matrix_name + " must \
be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    i = 0
    size = len(m_a[0])
    Row = len(m_b[0])
    Col = len(m_a)
    new_matrix = []

    while i < Col:
        j = 0
        tmp = []
        while j < Row:
            k, result = 0, 0
            while k < size:
                result += m_a[i][k] * m_b[k][j]
                k += 1
            tmp.append(result)
            j += 1
        new_matrix.append(tmp)
        i += 1

    return new_matrix
