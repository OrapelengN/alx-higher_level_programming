#!/usr/bin/python3

"""
This module defines a LockedClass that restricts dynamic attribute creation,
allowing only the 'first_name' attribute.
"""


class LockedClass:
    """
    A class that prevents dynamic attribute creation, except for 'first_name'.
    """
    __slots__ = ('first_name',)

    def __init__(self):
        """Initializes the LockedClass."""
        pass
