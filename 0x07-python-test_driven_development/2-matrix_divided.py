#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if the input divisor is a valid number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if the input divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if the input matrix is a valid matrix of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the input matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide each element in the input matrix by the input divisor and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]
    
    return result
