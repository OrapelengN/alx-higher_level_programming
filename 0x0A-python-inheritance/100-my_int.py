#!/usr/bin/python3
"""
Module 100-my_int
Contains a class MyInt that inherits from int and inverts == and !=.
"""


class MyInt(int):
    """
    A class MyInt that inherits from int and inverts == and !=.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The other value to compare.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The other value to compare.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
