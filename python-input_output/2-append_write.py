#!/usr/bin/python3
"""
Write a function that appends a string to a text file (UTF8)
and returns the num chars added
"""


def append_write(filename="", text=""):
    """
    Function to append to a file
    You don’t need to manage file permissions
      or file doesn't exist exceptions
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
