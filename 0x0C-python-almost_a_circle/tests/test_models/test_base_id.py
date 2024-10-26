import unittest
from models.base import Base


class TestBaseIDAssignment(unittest.TestCase):

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0  # Resetting the private class attribute

    def test_auto_id_increment(self):
        """Test that each instance of Base has an ID that increments by 1."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test that a custom ID is assigned properly, without increment."""
        b4 = Base(10)
        b5 = Base()

        self.assertEqual(b4.id, 10)  # Custom ID
        self.assertEqual(b5.id, 1)   # Auto ID resumes from 1 after reset

    def test_mixed_id_assignment(self):
        """Test behavior with mixed custom and auto IDs."""
        b6 = Base()
        b7 = Base(100)
        b8 = Base()

        self.assertEqual(b6.id, 1)    # First auto-assigned ID
        self.assertEqual(b7.id, 100)  # Custom ID
        self.assertEqual(b8.id, 2)    # Next auto ID


if __name__ == "__main__":
    unittest.main()
