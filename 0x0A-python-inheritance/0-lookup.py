#!/usr/bin/python3
"""
Module 0-lookup
Contains a function that returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of the attributes and methods of the object.
    """
    return dir(obj)
