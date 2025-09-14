#!/usr/bin/python3
"""
This module contains one function for printing str arguments

"""

def say_my_name(first_name, last_name=""):
    """
    Print
      My name is <first name> <last name>

    Args:
      first_name : string containing first name
      last_name : optional string containing last name
        defaults to ""
    
    Returns:
      Nothing
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    
    if(type(last_name) is not str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))


    if __name__ == "__main__":
        import doctest
        doctest.testmod()