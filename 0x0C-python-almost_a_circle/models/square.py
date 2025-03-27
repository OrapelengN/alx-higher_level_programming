#!/usr/bin/python3
"""Module defining the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter for the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size."""
        self.width = value
        self.height = value
