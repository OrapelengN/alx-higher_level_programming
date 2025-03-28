#!/usr/bin/python3
"""Unittest for Base class."""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_auto_id_assignment(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_id_assignment(self):
        """Test manual ID assignment."""
        b4 = Base(10)
        b5 = Base(-5)
        b6 = Base(0)

        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 0)

    def test_mixed_id_assignment(self):
        """Test mixed ID assignment."""
        b1 = Base()
        b2 = Base(100)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)

    def test_private_attribute_access(self):
        """Test that the private attribute __nb_objects is not directly
        accessible."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()

    def test_to_json_string_rectangle(self):
        """Test to_json_string with Rectangle dictionaries."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        e_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_string, e_string)

    def test_to_json_string_square(self):
        """Test to_json_string with Square dictionaries."""
        s1 = Square(10, 2, 1, 1)
        dictionary = s1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_string = '[{"id": 1, "size": 10, "x": 2, "y": 1}]'
        self.assertEqual(json_string, expected_string)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_multiple_dictionaries(self):
        """Test to_json_string with multiple dictionaries."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        dictionary1 = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_string = Base.to_json_string([dictionary1, dictionary2])
        expected_string = '[{"id": 1, "width": 10, "height": 7, "x": 2,
                             "y": 8}, {"id": 2, "width": 2, "height": 4,
                                       "x": 0, "y": 0}]'
        self.assertEqual(json_string, expected_string)

    def test_to_json_string_type(self):
        """Test to_json_string return type."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 1, "width": 10, "height": 7, "x": 2,
                                  "y": 8}, {"id": 2, "width": 2, "height": 4,
                                            "x": 0, "y": 0}]'
            self.assertEqual(content, expected_content)

        os.remove("Rectangle.json")

    def test_save_to_file_square(self):
        """Test save_to_file with Square instances."""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(3, 1, 1, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 3, "size": 5, "x": 1, "y": 2},
                                 {"id": 4, "size": 3, "x": 1, "y": 1}]'
            self.assertEqual(content, expected_content)

        os.remove("Square.json")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        os.remove("Rectangle.json")

    def test_save_to_file_overwrite(self):
        """Test save_to_file overwrites existing file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])

        r2 = Rectangle(5, 3, 1, 4, 2)
        Rectangle.save_to_file([r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 2, "width": 5, "height": 3, "x": 1,
                                  "y": 4}]'
            self.assertEqual(content, expected_content)

        os.remove("Rectangle.json")

    def test_from_json_string_rectangle(self):
        """Test from_json_string with Rectangle dictionaries."""
        json_string = '[{"id": 89, "width": 10, "height": 4}, {"id": 7,
                                                               "width": 1,
                                                               "height": 7}]'
        list_output = Base.from_json_string(json_string)
        expected_output = [{"id": 89, "width": 10, "height": 4}, {"id": 7,
                                                                  "width": 1,
                                                                  "height": 7}]
        self.assertEqual(list_output, expected_output)

    def test_from_json_string_square(self):
        """Test from_json_string with Square dictionaries."""
        json_string = '[{"id": 1, "size": 5, "x": 1, "y": 2}, {"id": 2,
                                                               "size": 3,
                                                               "x": 1,
                                                               "y": 1}]'
        list_output = Base.from_json_string(json_string)
        expected_output = [{"id": 1, "size": 5, "x": 1, "y": 2}, {"id": 2,
                                                                  "size": 3,
                                                                  "x": 1,
                                                                  "y": 1}]
        self.assertEqual(list_output, [{"id": 1, "size": 5, "x": 1, "y": 2},
                                       {"id": 2, "size": 3, "x": 1, "y": 1}])

    def test_from_json_string_empty_string(self):
        """Test from_json_string with empty string."""
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_type(self):
        """Test from_json_string return type."""
        json_string = '[{"id": 89, "width": 10, "height": 4}]'
        list_output = Base.from_json_string(json_string)
        self.assertIsInstance(list_output, list)

    def test_create_rectangle(self):
        """Test create method with Rectangle dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_square(self):
        """Test create method with Square dictionary."""
        s1 = Square(5, 1, 2, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_create_invalid_class(self):
        """Test create method with invalid class."""
        class InvalidClass(Base):
            pass
        invalid_instance = InvalidClass.create(id=1)
        self.assertIsNone(invalid_instance)

    # Added tests for the cases in the question
    def test_create_rectangle_simple(self):
        r = Rectangle.create(**{'width': 2, 'height': 3})
        self.assertIsInstance(r, Rectangle)

    def test_create_rectangle_x(self):
        r = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12})
        self.assertIsInstance(r, Rectangle)

    def test_create_rectangle_x_y(self):
        r = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1})
        self.assertIsInstance(r, Rectangle)

    def test_create_rectangle_x_y_id(self):
        r = Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1,
                                                                  'id': 89})
        self.assertIsInstance(r, Rectangle)

    def test_create_square_simple(self):
        s = Square.create(**{'size': 2})
        self.assertIsInstance(s, Square)

    def test_create_square_x(self):
        s = Square.create(**{'size': 2, 'x': 1})
        self.assertIsInstance(s, Square)

    def test_create_square_x_y(self):
        s = Square.create(**{'size': 2, 'x': 1, 'y': 3})
        self.assertIsInstance(s, Square)

    def test_create_square_x_y_id(self):
        s = Square.create(**{'size': 2, 'x': 1, 'y': 3, 'id': 89})
        self.assertIsInstance(s, Square)

    def test_load_from_file_rectangle(self):
        """Test load_from_file with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(str(r1), str(loaded_rectangles[0]))
        self.assertEqual(str(r2), str(loaded_rectangles[1]))

        os.remove("Rectangle.json")

    def test_load_from_file_square(self):
        """Test load_from_file with Square instances."""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(3, 1, 1, 4)
        Square.save_to_file([s1, s2])

        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(str(s1), str(loaded_squares[0]))
        self.assertEqual(str(s2), str(loaded_squares[1]))

        os.remove("Square.json")

    def test_load_from_file_empty(self):
        """Test load_from_file with non-existent file."""
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(loaded_rectangles, [])

    def test_load_from_file_non_existent(self):
        """Test load_from_file with non-existent file."""
        os.remove("Rectangle.json")
        if os.path.exists("Rectangle.json")
        else None
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_to_file_csv_rectangle(self):
        """Test save_to_file_csv with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])

        self.assertTrue(os.path.exists("Rectangle.csv"))  # check if file exist
        with open("Rectangle.csv", "r") as f:
            content = f.read()
            self.assertEqual(content, "1,10,7,2,8\n2,2,4,0,0\n")

        os.remove("Rectangle.csv")

    def test_save_to_file_csv_square(self):
        """Test save_to_file_csv with Square instances."""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(3, 1, 1, 4)
        Square.save_to_file_csv([s1, s2])

        self.assertTrue(os.path.exists("Square.csv"))  # Check if file exists
        with open("Square.csv", "r") as f:
            content = f.read()
            self.assertEqual(content, "3,5,1,2\n4,3,1,1\n")

        os.remove("Square.csv")

    def test_load_from_file_csv_rectangle(self):
        """Test load_from_file_csv with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])

        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(str(r1), str(loaded_rectangles[0]))
        self.assertEqual(str(r2), str(loaded_rectangles[1]))

        os.remove("Rectangle.csv")

    def test_load_from_file_csv_square(self):
        """Test load_from_file_csv with Square instances."""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(3, 1, 1, 4)
        Square.save_to_file_csv([s1, s2])

        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(str(s1), str(loaded_squares[0]))
        self.assertEqual(str(s2), str(loaded_squares[1]))

        os.remove("Square.csv")

    def test_load_from_file_csv_empty(self):
        """Test load_from_file_csv with non-existent file."""
        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(loaded_rectangles, [])

    def test_load_from_file_csv_non_existent(self):
        """Test load_from_file_csv with non-existent file."""
        os.remove("Rectangle.csv") if os.path.exists("Rectangle.csv") else None
        self.assertEqual(Rectangle.load_from_file_csv(), [])
