#!/usr/bin/python3
"""
Module 7-base_geometry
Contains a class BaseGeometry with an area method and integer validator.
"""


class BaseGeometry:
    """
    A class BaseGeometry with an area method and integer validator.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable (for error message).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


# Add the following to capture the output of the print statement.
def capture_and_print(e):
    output = f"{e.__class__.__name__}: {e}"
    print(repr(output))  # Print the raw representation of the output.


# Modify the doctest to use the capture_and_print function.
if __name__ == "__main__":
    BaseGeometry = BaseGeometry
    bg = BaseGeometry()
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        capture_and_print(e)
    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        capture_and_print(e)
    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        capture_and_print(e)
    try:
        bg.integer_validator("test", 0.1)
    except Exception as e:
        capture_and_print(e)
    try:
        bg.integer_validator("test", None)
    except Exception as e:
        capture_and_print(e)
    try:
        bg.integer_validator("test", [])
    except Exception as e:
        capture_and_print(e)
