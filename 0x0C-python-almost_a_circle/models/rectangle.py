#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

        @property
        def width(self):
            """Set/get the width of the Rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.validate_integer("width", value)
            self.validate_positive("width", value)
            self.__width = value

        @property
        def height(self):
            """Set/get the height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integeri")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.validate_integer("height", value)
            self.validate_positive("height", value)
            self.__height = value

        @property
        def x(self):
            """Set/get the x coordinate of the Rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.validate_integer("x", value)
            self.validate_non_negative("x", value)
            self.__x = value

        @property
        def y(self):
            """Set/get the y coordinate of the Rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.validate_integer("y", value)
            self.validate_non_negative("y", value)
            self.__y = value

        def area(self):
            """Return the area of the rectangle"""
            return self.width * self.height

        def display(self):
            """Print the rectangle instance using the '#' character with x and y offsets"""
            for _ in range(self.y):
                print()

            for _ in range(self.height):
                print(' ' * self.x + '#' * self.width)

        def __str__(self):
            """Return the string representation of the Rectangle"""
            return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
