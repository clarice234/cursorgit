import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('buggy_max.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def find_max(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): List of numbers to find maximum from
    
    Returns:
        float/int: Maximum value in the list
    """
    logger.info(f"Starting max calculation for list: {numbers}")
    
    # Check for empty list
    if not numbers:
        logger.warning("Empty list provided - returning 0 (this is a bug!)")
        return 0
    
    logger.info(f"List length: {len(numbers)}")
    
    # Initialize max_val to 0 (THIS IS THE BUG!)
    max_val = 0
    logger.info(f"Initial max_val set to: {max_val} (BUG: should be first element)")
    
    # Iterate through the list
    for i, n in enumerate(numbers):
        logger.info(f"Checking element {i}: {n}")
        
        if n > max_val:
            logger.info(f"Found new max: {n} > {max_val}")
            max_val = n
        else:
            logger.info(f"Element {n} is not greater than current max {max_val}")
    
    logger.info(f"Final max_val: {max_val}")
    
    # Log the bug for negative numbers
    if all(n < 0 for n in numbers):
        logger.error(f"BUG DETECTED: All numbers are negative {numbers}, but returning {max_val}")
        logger.error("The function should return the largest negative number, not 0")
    
    return max_val
