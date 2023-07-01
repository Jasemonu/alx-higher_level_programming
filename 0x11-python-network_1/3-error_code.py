#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from sys import argv
from urllib import request, error


if __name__ == "__main__":

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read(url).decode("ascii")
            print(body)
    except error.HTTPError as e:
        print("Error code: {}" .format(e.code))
