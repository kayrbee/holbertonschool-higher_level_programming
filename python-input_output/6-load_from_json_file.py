#!/usr/bin/python3
"""
Write a function that creates
an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Function to create obj from json file
    You don’t need to manage exceptions
      if the JSON string doesn’t represent an object.
    You don’t need to manage file permission exceptions.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
