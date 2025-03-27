#!/usr/bin/python3
"""Module defining the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x-coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y-coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def area(self):
        """Calculates and returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character '#'."""
        for _ in range(self.__height):
            print("#" * self.__width)
