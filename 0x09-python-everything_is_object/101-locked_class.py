#!/usr/bin/python3
"""Defining a locked class"""


class LockedClass:
    """This magic method prevents dynamically creation\
        of new instance attributes excet first_name
    """

    __slots__ = ["first_name"]
