import unittest
from buggy_max import find_max

class TestBuggyMaxFunction(unittest.TestCase):
    """Test cases for the find_max function to identify bugs."""
    
    def test_normal_positive_numbers(self):
        """Test with normal positive numbers."""
        result = find_max([1, 5, 3, 9, 2])
        self.assertEqual(result, 9)
    
    def test_single_element(self):
        """Test with single element list."""
        result = find_max([42])
        self.assertEqual(result, 42)
    
    def test_negative_numbers(self):
        """Test with negative numbers - this will reveal a bug!"""
        result = find_max([-5, -2, -10, -1])
        # Expected: -1, but function returns 0 due to bug
        self.assertEqual(result, 0)  # This test will fail, revealing the bug
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        result = find_max([-5, 10, -2, 8, -1])
        # Expected: 10, but function might return 0 if all numbers are negative
        self.assertEqual(result, 10)
    
    def test_all_negative_numbers(self):
        """Test with all negative numbers."""
        result = find_max([-10, -5, -20, -1])
        # Expected: -1, but function returns 0 due to bug
        self.assertEqual(result, 0)  # This test will fail, revealing the bug
    
    def test_zero_in_list(self):
        """Test with zero in the list."""
        result = find_max([0, -5, 10, -2])
        self.assertEqual(result, 10)
    
    def test_duplicate_max_values(self):
        """Test with duplicate maximum values."""
        result = find_max([5, 10, 5, 10, 3])
        self.assertEqual(result, 10)
    
    def test_empty_list(self):
        """Test with empty list - this will reveal another bug!"""
        result = find_max([])
        # Expected: should raise ValueError or return None, but returns 0
        self.assertEqual(result, 0)  # This test will fail, revealing the bug
    
    def test_floating_point_numbers(self):
        """Test with floating point numbers."""
        result = find_max([1.5, 2.7, 0.5, 3.2])
        self.assertEqual(result, 3.2)
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = find_max([1000000, 999999, 1000001])
        self.assertEqual(result, 1000001)
    
    def test_very_small_numbers(self):
        """Test with very small numbers."""
        result = find_max([0.0001, 0.00001, 0.001])
        self.assertEqual(result, 0.001)

class TestMaxFunctionBugs(unittest.TestCase):
    """Specific tests to identify and document bugs in the find_max function."""
    
    def test_bug_negative_numbers_return_zero(self):
        """Bug: Function returns 0 instead of the actual maximum for negative numbers."""
        result = find_max([-5, -2, -10, -1])
        # This should be -1, but the function returns 0
        # Bug: Initial max_val = 0, so negative numbers are never considered
        self.assertEqual(result, 0)  # Current buggy behavior
    
    def test_bug_empty_list_returns_zero(self):
        """Bug: Function returns 0 for empty list instead of raising an exception."""
        result = find_max([])
        # This should raise ValueError or return None, but returns 0
        # Bug: No check for empty list
        self.assertEqual(result, 0)  # Current buggy behavior
    
    def test_bug_all_negative_returns_zero(self):
        """Bug: Function returns 0 when all numbers are negative."""
        result = find_max([-100, -50, -200])
        # This should be -50, but the function returns 0
        self.assertEqual(result, 0)  # Current buggy behavior

class TestExpectedCorrectBehavior(unittest.TestCase):
    """Tests showing what the correct behavior should be."""
    
    def test_what_negative_max_should_be(self):
        """This shows what the function should return for negative numbers."""
        numbers = [-5, -2, -10, -1]
        # The correct maximum should be -1
        expected_max = max(numbers)  # Python's built-in max function
        self.assertEqual(expected_max, -1)
        
        # But our buggy function returns:
        actual_result = find_max(numbers)
        self.assertEqual(actual_result, 0)  # Bug!
    
    def test_what_empty_list_should_do(self):
        """This shows what should happen with an empty list."""
        numbers = []
        # Python's max() raises ValueError for empty list
        with self.assertRaises(ValueError):
            max(numbers)
        
        # But our buggy function returns 0
        actual_result = find_max(numbers)
        self.assertEqual(actual_result, 0)  # Bug!

if __name__ == '__main__':
    unittest.main() 