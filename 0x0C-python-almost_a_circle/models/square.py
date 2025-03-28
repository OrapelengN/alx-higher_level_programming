#!/usr/bin/python3
"""Module defining the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes based on args and kwargs."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise AttributeError("Invalid attribute: {}".format(key))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
