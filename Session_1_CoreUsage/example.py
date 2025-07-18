import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('discount_calculation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def get_discounted_price(price, discount_percent):
    """
    Calculate the discounted price based on original price and discount percentage.
    
    Args:
        price (float): Original price
        discount_percent (float): Discount percentage (0-100)
    
    Returns:
        float: Final discounted price
    """
    logger.info(f"Starting discount calculation - Price: {price}, Discount: {discount_percent}%")
    
    # Validate inputs
    if price <= 0:
        logger.warning(f"Invalid price: {price}. Price must be positive.")
        return 0
    
    if discount_percent < 0:
        logger.warning(f"Invalid discount percentage: {discount_percent}%. Discount cannot be negative.")
        return 0
    
    logger.info(f"Input validation passed - Price: {price}, Discount: {discount_percent}%")
    
    # Calculate discount amount
    discount_amount = price * discount_percent / 100
    logger.info(f"Calculated discount amount: {discount_amount}")
    
    # Calculate final price
    final_price = price - discount_amount
    logger.info(f"Calculated final price: {final_price}")
    
    logger.info(f"Discount calculation completed - Original: {price}, Final: {final_price}")
    return final_price
