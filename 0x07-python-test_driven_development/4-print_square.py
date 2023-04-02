#!/usr/bin/python3

"""

This module contains a function that prints squares of a given size

"""

def print_square(size):
    
    """

    Prints a square made out of the character '#'
    
    Arguaments:
    size -- the size of the square (an integer)
    
    Returns:
    None

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    
    
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for square in range(size):
        print("#" * size)
