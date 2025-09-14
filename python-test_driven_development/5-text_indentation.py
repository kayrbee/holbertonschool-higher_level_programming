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

    #  handle periods  
    p_chunk = [sentence for sentence in text.split(".")]
    p = ".***".join(p_chunk)
    # print(p)

    #   handle question marks
    q_chunk = [sentence for sentence in p.split("?")]
    q = "?***".join(q_chunk)
    # print(q)

    #   handle colons
    c_chunk = [sentence for sentence in q.split(":")]
    c = ":***".join(c_chunk)
    # print(c)

    #  strip spaces at start of sentences
    w_parse = [word for word in c.split('*** ')]
    print("w_parse: ", w_parse)
    w = "***".join(w_parse)
    print("w: ", w)

    chunk = [sentence for sentence in w.split("***")]
    for i, ch in enumerate(chunk):
        if i < len(chunk) - 1:
            print("{}".format(ch), end='\n\n')



text = "string to print. second string? third string: fourth string?"
text_indentation(text)
