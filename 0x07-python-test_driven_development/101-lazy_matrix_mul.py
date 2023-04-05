#!/usr/bi/python3
"""A module that contains a function that returns the\
   product of two matrices

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Afunction that returns the product of two matrices

       Arg:
        m_a: represents the first matrix
        m_b: represents the second matrix

    """

    return (np.matmul(m_a, m_b))
