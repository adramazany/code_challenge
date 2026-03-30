from unittest import TestCase
from src import Statistics

class TestStatistics(TestCase):
    """
    Unit tests for the DataProcessor class.
    """

    def setUp(self):
        """Set up a fresh DataProcessor instance before each test."""
        self.statistics = Statistics()

    def test_multiply_valid_input(self):
        """Test multiplication with positive floats."""
        result = self.statistics.multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)

    def test_safe_divide_by_zero_raises_error(self):
        """Ensure dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.statistics.safe_divide(10, 0)
