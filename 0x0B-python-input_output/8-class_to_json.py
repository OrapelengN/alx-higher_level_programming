#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description with
simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an
object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object's serializable
        attributes.
    """
    return {attr: getattr(obj, attr) for attr in obj.__dict__}
