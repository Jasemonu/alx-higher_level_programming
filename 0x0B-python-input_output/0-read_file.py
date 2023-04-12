#!/usr/bin/python3
""" A function that reads a file and prints to the stdout"""


def read_file(filename=""):

    """Arg: filename: Name of the file to be read from"""

    with open(filename, "r", encoding="utf-8") as fl:
        text = fl.read()
    print(text, end="")
