#!/usr/bin/python3
"""
This module defines a Student class with JSON serialization,
attribute filtering, and JSON reloading.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age, with JSON
    serialization and reloading.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): A dictionary representing the student's attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
