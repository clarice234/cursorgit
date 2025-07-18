import unittest
from example import get_discounted_price

class TestDiscountCalculation(unittest.TestCase):
    """Test cases for the get_discounted_price function."""
    
    def test_normal_discount(self):
        """Test normal discount calculation."""
        result = get_discounted_price(100, 20)
        self.assertEqual(result, 80)
    
    def test_zero_discount(self):
        """Test with zero discount."""
        result = get_discounted_price(100, 0)
        self.assertEqual(result, 100)
    
    def test_full_discount(self):
        """Test with 100% discount."""
        result = get_discounted_price(100, 100)
        self.assertEqual(result, 0)
    
    def test_negative_price(self):
        """Test with negative price."""
        result = get_discounted_price(-50, 10)
        self.assertEqual(result, 0)
    
    def test_zero_price(self):
        """Test with zero price."""
        result = get_discounted_price(0, 20)
        self.assertEqual(result, 0)
    
    def test_negative_discount(self):
        """Test with negative discount percentage."""
        result = get_discounted_price(100, -10)
        self.assertEqual(result, 0)
    
    def test_decimal_discount(self):
        """Test with decimal discount percentage."""
        result = get_discounted_price(100, 12.5)
        self.assertEqual(result, 87.5)
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = get_discounted_price(10000, 15)
        self.assertEqual(result, 8500)

if __name__ == '__main__':
    unittest.main() 