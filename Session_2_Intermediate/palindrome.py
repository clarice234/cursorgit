import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('palindrome_detection.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def is_palindrome(word):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        word (str): The string to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    logger.info(f"Starting palindrome check for: '{word}'")
    
    # Handle empty string
    if not word:
        logger.info("Empty string detected - considered palindrome")
        return True
    
    logger.info(f"Original string length: {len(word)}")
    
    # Clean the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    logger.info(f"Cleaned string: '{cleaned}' (length: {len(cleaned)})")
    
    # Handle single character
    if len(cleaned) <= 1:
        logger.info("Single character or empty after cleaning - considered palindrome")
        return True
    
    # Check if cleaned string equals its reverse
    reversed_string = cleaned[::-1]
    logger.info(f"Reversed string: '{reversed_string}'")
    
    is_palindrome_result = cleaned == reversed_string
    logger.info(f"Palindrome check result: {is_palindrome_result}")
    
    if is_palindrome_result:
        logger.info(f"'{word}' is a palindrome")
    else:
        logger.info(f"'{word}' is not a palindrome")
    
    return is_palindrome_result
