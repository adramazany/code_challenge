"""
Module for processing data with clean code standards.
"""

class Statistics:
    """
    A class to handle data transformations and calculations.
    """

    def multiply(self, factor_a: float, factor_b: float) -> float:
        """
        Calculates the product of two numbers.

        Args:
            factor_a: The first numeric factor.
            factor_b: The second numeric factor.

        Returns:
            The product of factor_a and factor_b.
        """
        return factor_a * factor_b

    def safe_divide(self, dividend: float, divisor: float) -> float:
        """
        Safely divides two numbers, handling zero-division errors.

        Returns:
            The quotient of the division.

        Raises:
            ValueError: If the divisor is zero.
        """
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        return dividend / divisor
