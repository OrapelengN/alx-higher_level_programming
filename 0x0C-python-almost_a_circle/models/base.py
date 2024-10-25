#!/usr/bin/python3
"""Defines a base class."""

# models/base.py
import json
import os
import csv


class Base:
    """Base class to manage the id attribute for future classes."""

    __nb_objects = 0  # Private class attribute to track number of instances

    def __init__(self, id=None):
        """Initialize the Base class with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        # Create a dummy instance based on the class type
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # minimal width and height for Rectangle
        elif cls.__name__ == "Square":
            dummy = cls(1)  # minimal size for Square

        # Update dummy instance with actual attributes
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"

        # Check if the file exists
        if not os.path.exists(filename):
            return []

        # Read the JSON file
        with open(filename, "r") as file:
            json_data = file.read()

        # Convert JSON string to list of dictionaries
        list_dicts = cls.from_json_string(json_data)

        # Convert each dictionary to an instance using the create method
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                     obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from a CSV file and returns a list of instances."""
        filename = f"{cls.__name__}.csv"
        instances = []
        try:
            with open(filename, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        dictionary = {
                                'id': int(row[0]),
                                'width': int(row[1]),
                                'height': int(row[2]),
                                'x': int(row[3]),
                                'y': int(row[4])
                                }
                    elif cls.__name__ == 'Square':
                        dictionary = {
                                'id': int(row[0]),
                                'size': int(row[1]),
                                'x': int(row[2]),
                                'y': int(row[3])
                                }
                        instance = cls.create(**dictionary)
                        instances.append(instance)
        except FileNotFoundError:
            return instances
        return instances

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
