import unittest
from palindrome import is_palindrome

class TestPalindromeDetection(unittest.TestCase):
    """Test cases for the is_palindrome function."""
    
    def test_simple_palindrome(self):
        """Test simple palindrome words."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("deed"))
    
    def test_non_palindrome(self):
        """Test non-palindrome words."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
    
    def test_case_insensitive(self):
        """Test that function is case insensitive."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("LEVEL"))
        self.assertTrue(is_palindrome("DeEd"))
    
    def test_with_spaces(self):
        """Test palindromes with spaces."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("a man a plan a canal panama"))
        self.assertTrue(is_palindrome("never odd or even"))
    
    def test_with_punctuation(self):
        """Test palindromes with punctuation."""
        self.assertTrue(is_palindrome("race, car!"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Madam, I'm Adam."))
    
    def test_numbers_and_letters(self):
        """Test with numbers and letters mixed."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("abc12321cba"))
        self.assertFalse(is_palindrome("12345"))
    
    def test_single_character(self):
        """Test single character strings."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("5"))
        self.assertTrue(is_palindrome("!"))
    
    def test_empty_string(self):
        """Test empty string."""
        self.assertTrue(is_palindrome(""))
    
    def test_whitespace_only(self):
        """Test strings with only whitespace."""
        self.assertTrue(is_palindrome("   "))
        self.assertTrue(is_palindrome("\t\n"))
    
    def test_mixed_case_with_special_chars(self):
        """Test complex cases with mixed case and special characters."""
        self.assertTrue(is_palindrome("A1b2c3c2b1a"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(is_palindrome("This is not a palindrome"))

if __name__ == '__main__':
    unittest.main() 