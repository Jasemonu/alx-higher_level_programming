#!/usr/bin/python3
"""function that appends a string at the end of a text
   file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
     Args:
        Filename (str): Name of the file to append to.
        Text (str): Text to be appended to the file.
     Returns:
        int: Number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
