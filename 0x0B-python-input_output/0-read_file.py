#!/usr/bin/python3
""" A function that reads a file and prints to the stdout"""


def read_file(filename=""):

    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fl:
        print(fil.read(), end="")
