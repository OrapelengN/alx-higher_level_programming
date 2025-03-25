#!/usr/bin/python3
"""
Module 1-my_list
Contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class MyList that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        print(sorted(self))
