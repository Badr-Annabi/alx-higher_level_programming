#!/usr/bin/python3
"""
lazy_matrix_mul module

Defines a matrix multiplication function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Return the multiplication of two matrices.

    Args:
        m_a: list of lists of ints orfloats.
        m_b: list of lists of ints or floats.
    """
    return (np.matmul(m_a, m_b))
