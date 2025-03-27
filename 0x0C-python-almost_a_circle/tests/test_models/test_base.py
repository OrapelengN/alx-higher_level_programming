#!/usr/bin/python3
"""Unittest for Base class."""

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
        expected_string = '[{"id": 1, "width": 10,
                             "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_string, expected_string)

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
