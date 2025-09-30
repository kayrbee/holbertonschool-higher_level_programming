#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function to read a file
    You don’t need to manage file permission or file doesn't exist exceptions.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
