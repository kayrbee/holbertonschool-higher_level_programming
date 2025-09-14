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

    # Create a placeholder string with standardised delimiters
    #   The original delimiter from the print string must be retained
    #   Spaces at sentence boundaries must be skipped
    for marker in markers:
        if marker != '*** ':
            delimiter = marker + '***'
        else:
            delimiter = '***'
        split_chunk = [sentence for sentence in text_copy.split(marker)]
        text_copy = delimiter.join(split_chunk)

    chunk_to_print = [sentence for sentence in text_copy.split("***")]
    for ch in chunk_to_print:
        if len(chunk_to_print) == 1 and text_copy[-3:] != '***':
            length = len(text_copy)
            text_copy = text_copy[:length - 3]
            print("{}".format(ch), end='')
        else:
            print("{}".format(ch), end='\n\n')

# text = "string to print. second string? third string: fourth string?"
# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
# Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
# Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
# Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
# Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
# rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
# stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
# cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
# beatiorem! Iam ruinas videres"""
# text = 'Holberton School'
# text_indentation(text)
# text_indentation("Holberton School. 123")
# text_indentation("Holberton.School")
