#!/usr/bin/python3
"""
Module 10-square
Contains a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return super().area()
