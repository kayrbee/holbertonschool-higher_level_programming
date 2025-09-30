#!/usr/bin/python3
"""
Write a function that writes an Object
to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function to write json to file
    You don’t need to manage exceptions
      if the object can’t be serialized.
    You don’t need to manage file permission exceptions.
    """
    with open(filename, "w", encoding="utf-8") as f:
        o = json.dumps(my_obj)
        f.write(o)
