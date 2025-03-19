#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents dynamic attribute creation, except for 'first_name'.
    """
    __slots__ = ('first_name',)

    def __init__(self):
        """Initializes the LockedClass."""
        pass
