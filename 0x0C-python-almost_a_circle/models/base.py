#!/usr/bin/python3
"""Defines a base class."""

import json
import os
import csv
import turtle


class Base:
    """Base class to manage the id attribute for future classes."""

    __nb_objects = 0  # Private class attribute to track number of instances

    def __init__(self, id=None):
        """Initializes a Base instance.

        Args:
            id (int): The id of the instance. If None, a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            json_data = file.read()
        list_dicts = cls.from_json_string(json_data)
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
            # don't return instances, it's already initiated as an empty list.
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares using Turtle graphics."""

        screen = turtle.Screen()
        screen.title("Draw Rectangles and Squares")
        turtle.speed("fastest")

        def draw_shape(x, y, width, height, color):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(height)
                turtle.left(90)
            turtle.end_fill()

        for rect in list_rectangles:
            draw_shape(rect.x, rect.y, rect.width, rect.height, "blue")

        for square in list_squares:
            draw_shape(square.x, square.y, square.size, square.size, "green")

        turtle.done()


if __name__ == "__main__":
    s = Square.create(**{'size': 2, 'x': 1, 'y': 3, 'id': 89})
    if isinstance(s, Square):
        print("OK")
