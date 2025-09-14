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
    
    markers = ['.', '?', ':', '*** ']
    text_copy = text[:]

    #   Create a placeholder string with standardised delimiters
    #   Remove space at sentence boundaries
    for marker in markers:
        if marker != '*** ':
            delimiter = marker + '***'
        else:
            delimiter = '***'
        split_chunk = [sentence for sentence in text_copy.split(marker)]
        text_copy = delimiter.join(split_chunk)
    
    if text_copy[-3:] == '***':
        length = len(text_copy)
        text_copy = text_copy[:length - 3]

    chunk_to_print = [sentence for sentence in text_copy.split("***")]
    for ch in chunk_to_print:
        print("{}".format(ch), end='\n\n')

# text = "string to print. second string? third string: fourth string?"
# text_indentation(text)
