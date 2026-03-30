import unittest
from src.processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    """
    Unit tests for the DataProcessor class.
    """

    def setUp(self):
        """Set up a fresh DataProcessor instance before each test."""
        self.processor = DataProcessor()

    def test_multiply_valid_input(self):
        """Test multiplication with positive floats."""
        result = self.processor.multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)

    def test_divide_by_zero_raises_error(self):
        """Ensure dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.processor.safe_divide(10, 0)

if __name__ == '__main__':
    unittest.main()
