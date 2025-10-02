#!/usr/bin/python3
"""
Write a module that serialises and deserialises to/from json
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialise data and save to a file
    """
    # jd = json.dumps(data)
    with open(filename, "w", encoding="utf-8") as f:
        # filename.write(jd)
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialise data from a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
