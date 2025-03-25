#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
