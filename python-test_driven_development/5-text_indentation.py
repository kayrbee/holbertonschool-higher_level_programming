#!/usr/bin/python3
"""
Module contains one function to format a text block
"""


def text_indentation(text):
    """
    Prints two new lines after each of `.` `?` or `:`

    Args:
      text : contains a block of text

    Returns: nothing
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    chunk = [sentence for sentence in text.split(". ")]
    last = len(chunk)

    for pos, ch in enumerate(chunk):
        if pos != last - 1:
            print("{}".format(ch), end='.\n\n')
        else:
            print("{}".format(ch), end='\n\n')

# text = "string to print. second string?"
# text_indentation(text)
