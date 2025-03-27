#!/usr/bin/python3
"""Unittest for Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init_valid(self):
        """Test initialization with valid values."""
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_init_invalid_width(self):
        """Test initialization with invalid width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 5)

    def test_init_invalid_height(self):
        """Test initialization with invalid height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "5")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -5)

    def test_init_invalid_x(self):
        """Test initialization with invalid x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 5, -2)

    def test_init_invalid_y(self):
        """Test initialization with invalid y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 5, 2, -3)

    def test_width_setter_invalid(self):
        """Test width setter with invalid values."""
        r = Rectangle(10, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "10"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_height_setter_invalid(self):
        """Test height setter with invalid values."""
        r = Rectangle(10, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "5"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -5

    def test_x_setter_invalid(self):
        """Test x setter with invalid values."""
        r = Rectangle(10, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = "2"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -2

    def test_y_setter_invalid(self):
        """Test y setter with invalid values."""
        r = Rectangle(10, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "3"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -3


if __name__ == '__main__':
    unittest.main()

    def test_area(self):
        """Test area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        r4 = Rectangle(1, 1)
        self.assertEqual(r4.area(), 1)

    def test_area_with_invalid_dimensions(self):
        """Test area with invalid dimensions."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = 0
            r.area()

        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.height = 0
            r.area()

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.height = "string"
            r.area()

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "string"
            r.area()

    def test_display(self):
        """Test display method."""
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

        r2 = Rectangle(2, 2)
        expected_output_2 = "##\n##\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output_2)

    def test_display_with_invalid_dimensions(self):
        """Test display with invalid dimensions."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = 0
            r.display()

        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.height = 0
            r.display()

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.height = "string"
            r.display()

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "string"
            r.display()

    def test_str(self):
        """Test __str__ method."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

        r3 = Rectangle(1, 1)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 1/1")

    def test_str_with_invalid_attributes(self):
        """Test __str__ with invalid attributes."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = 0
            str(r)

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.height = "test"
            str(r)
