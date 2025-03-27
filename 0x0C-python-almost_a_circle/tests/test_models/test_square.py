#!/usr/bin/python3
"""Unittest for Square class."""

import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_init(self):
        """Test initialization."""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 12)

    def test_area(self):
        """Test area method."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        """Test display method."""
        s1 = Square(5)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

        s2 = Square(2, 2)
        expected_output_2 = "  ##\n  ##\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        s2.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output_2)

        s3 = Square(3, 1, 3)
        expected_output_3 = "\n\n\n ###\n ###\n ###\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        s3.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output_3)

    def test_str(self):
        """Test __str__ method."""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(str(s3), "[Square] (12) 1/3 - 3")

    def test_init_invalid_size(self):
        """Test initialization with invalid size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_init_invalid_x(self):
        """Test initialization with invalid x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -2)

    def test_init_invalid_y(self):
        """Test initialization with invalid y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -3)

    def test_size_getter_setter(self):
        """Test size getter and setter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid_values(self):
        """Test size setter with invalid values."""
        s = Square(5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "invalid"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1

    def test_size_getter_setter_with_other_attributes(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.size, 2)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 5)

    def test_update_args(self):
        """Test update method with *args."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

        s.update(1, 2)
        self.assertEqual(s.size, 2)

        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)

        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

        s.update(size=7, id=89, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.y, 1)

    def test_update_args_kwargs(self):
        """Test update method with *args and **kwargs."""
        s = Square(5)
        s.update(10, 2, x=3, y=4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)  # args override kwargs
        self.assertEqual(s.y, 0)

    def test_update_invalid_values(self):
        """Test update method with invalid values."""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.update(size="invalid")
        with self.assertRaises(ValueError):
            s.update(size=0)

        with self.assertRaises(TypeError):
            s.update(x="invalid")
        with self.assertRaises(ValueError):
            s.update(x=-1)

        with self.assertRaises(TypeError):
            s.update(y="invalid")
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_update_invalid_attribute(self):
        """Test update method with invalid attribute in **kwargs."""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.update(invalid_attribute=10)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 12)
        expected_dict = {"id": 12, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

        s2 = Square(1, 1)
        expected_dict2 = {"id": 1, "size": 1, "x": 0, "y": 0}
        self.assertEqual(s2.to_dictionary(), expected_dict2)

    def test_to_dictionary_with_updated_attributes(self):
        """Test to_dictionary with updated attributes."""
        s = Square(10, 2, 1, 12)
        s.update(size=5, x=3, y=4, id=15)
        expected_dict = {"id": 15, "size": 5, "x": 3, "y": 4}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_type(self):
        """Test to_dictionary return type."""
        s = Square(10, 2, 1, 12)
        self.assertIsInstance(s.to_dictionary(), dict)
