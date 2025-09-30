#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
and returns the num chars written
"""


def write_file(filename="", text=""):
    """
    Function to write to a file
    You don’t need to manage file permissions
    If file doesn't exist, creates it
    Overwrites contents if file exists
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
