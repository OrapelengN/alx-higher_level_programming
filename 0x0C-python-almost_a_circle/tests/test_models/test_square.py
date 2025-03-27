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
