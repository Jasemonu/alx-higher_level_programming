#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns the sum of two integers or floats as an integer.

    Args:
        a: the first argument, which must be an integer or float.
        b: the second argument, which must be an integer or float. Defaults to 98.

    Returns:
        The sum of the two arguments as an integer.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
