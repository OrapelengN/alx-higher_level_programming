#!/usr/bin/python3
"""Defines a base class."""


class Base:
    """Base class to manage the id attribute for future classes."""

    __nb_objects = 0  # Private class attribute to track number of instances

    def __init__(self, id=None):
        """Initialize the Base class with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
