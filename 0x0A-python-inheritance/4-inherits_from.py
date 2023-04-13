#!/usr/bin/python3
"""checks if class is inherited"""


def inherits_from(obj, a_class):
    """returns"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
