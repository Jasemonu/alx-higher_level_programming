#!/usr/bin/python3
"""A funtion that writes into a file and returns the number of characters"""


def write_file(filename="", text=""):

    """
       Args:
          filename (str): Name of the file to write to.
          text (str): Text to be written to the file.
     Retursn:
            int: Number of characters to written to the file
    """
    with open(filename, "w", encoding="utf-8") as fl:
        fl.write(text)
        num_characters = len(text)
    return num_characters
