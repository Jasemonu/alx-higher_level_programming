#!/usr/bin/python3
""""
This module contains a function that prints a message
"""

def say_my_name(first_name, last_name=""):
    """ This function prints "My name is <first name> <last name>"
        
    Args:
        first_name: the first given name to be printed
        last_name: the second given name tobe printed

    Raises:
        TypeError if any of the arguaments is not a string data type

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}" .format(first_name, last_name))
