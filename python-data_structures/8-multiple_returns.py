#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    result = (length, first)
    return result

# Alternative approaches:

# Tests
# # sentence = "At school, I learnt C!"
# sentence = ""
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))
