#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""

# models/rectangle.py
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.


        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identifier for the Rectangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__validate_positive_integer("width", value)
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__validate_positive_integer("height", value)
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__validate_non_negative_integer("x", value)
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__validate_non_negative_integer("y", value)
            self.__y = value

        def __validate_positive_integer(self, name, value):
            """Validates that a value is a positive integer."""
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive integer")

        def __validate_non_negative_integer(self, name, value):
            """Validates that a value is a non-negative integer."""
            if type(value) is not int or value < 0:
                raise ValueErroe(f"{name} must be a non-negative integer")

        def validate_integer(self, name, value):
            """Validate that value is an integer"""
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")

        def validate_positive(self, name, value):
            """Validate that value is greater than 0"""
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

        def validate_non_negative(self, name, value):
            """Validate that value is greater than or equal to 0"""
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

        def area(self):
            """Return the area of the rectangle"""
            return self.width * self.height

        def display(self):
            """Print the rectangle instance using the '#' character
                                            with x and y offsets"""
            for _ in range(self.y):
                print()

            for _ in range(self.height):
                print(' ' * self.x + '#' * self.width)

        def update(self, *args, **kwargs):
            """Update attributes with *args based on the order: id,
                                            width, height, x, y"""
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

            if args:
                attributes = ["id", "width", "height", "x", "y"]
                for i, value in enumerate(args):
                    if i < len(attributes):
                        setattr(self, attributes[i], value)
            else:
                # Use **kwargs if *args is not provided
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

        def __str__(self):
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                           self.y, self.width,
                                                           self.height)

        def to_dictionary(self):
            """Return the dictionary representation of a Rectangle instance"""
            return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
