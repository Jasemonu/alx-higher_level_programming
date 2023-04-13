#!/usr/bin/python3
"""A funtion that checks whether an object is
   an instance of a class of a subclass
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
