import unittest
from utils import calculate_bmi

class TestBMICalculation(unittest.TestCase):
    """Test cases for the calculate_bmi function."""
    
    def test_normal_bmi_calculation(self):
        """Test normal BMI calculation."""
        # Height: 1.75m, Weight: 70kg -> BMI = 70 / (1.75^2) = 22.86
        result = calculate_bmi(1.75, 70)
        self.assertEqual(result, 22.86)
    
    def test_underweight_bmi(self):
        """Test BMI calculation for underweight."""
        # Height: 1.70m, Weight: 50kg -> BMI = 50 / (1.70^2) = 17.30
        result = calculate_bmi(1.70, 50)
        self.assertEqual(result, 17.30)
    
    def test_overweight_bmi(self):
        """Test BMI calculation for overweight."""
        # Height: 1.65m, Weight: 85kg -> BMI = 85 / (1.65^2) = 31.22
        result = calculate_bmi(1.65, 85)
        self.assertEqual(result, 31.22)
    
    def test_zero_height(self):
        """Test with zero height (should return None)."""
        result = calculate_bmi(0, 70)
        self.assertIsNone(result)
    
    def test_negative_height(self):
        """Test with negative height (should return negative BMI)."""
        result = calculate_bmi(-1.75, 70)
        self.assertEqual(result, 22.86)  # -1.75^2 = 3.0625, 70/3.0625 = 22.86
    
    def test_zero_weight(self):
        """Test with zero weight."""
        result = calculate_bmi(1.75, 0)
        self.assertEqual(result, 0.0)
    
    def test_negative_weight(self):
        """Test with negative weight."""
        result = calculate_bmi(1.75, -70)
        self.assertEqual(result, -22.86)
    
    def test_very_small_numbers(self):
        """Test with very small numbers."""
        result = calculate_bmi(0.1, 0.5)
        self.assertEqual(result, 50.0)
    
    def test_very_large_numbers(self):
        """Test with very large numbers."""
        result = calculate_bmi(2.5, 200)
        self.assertEqual(result, 32.0)
    
    def test_decimal_precision(self):
        """Test decimal precision of BMI calculation."""
        result = calculate_bmi(1.80, 75.5)
        self.assertEqual(result, 23.30)
    
    def test_string_input(self):
        """Test with string inputs (should return None due to exception)."""
        result = calculate_bmi("1.75", "70")
        self.assertIsNone(result)
    
    def test_none_input(self):
        """Test with None inputs (should return None due to exception)."""
        result = calculate_bmi(None, 70)
        self.assertIsNone(result)
        result = calculate_bmi(1.75, None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 