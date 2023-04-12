#!/usr/bin/python3
"""This function returns a JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Returns JSON representation of str"""
    json_str = json.dumps(my_obj)
    return json_str
