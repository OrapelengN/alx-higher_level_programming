#!/usr/bin/python3
"""Defines a square class."""

# models/square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method to return a formatted string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter for size, returning the width (or height)"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, setting both width and height, with validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
