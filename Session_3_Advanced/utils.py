import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bmi_calculation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) using height and weight.
    
    Args:
        height (float): Height in meters
        weight (float): Weight in kilograms
    
    Returns:
        float: BMI value rounded to 2 decimal places, or None if calculation fails
    """
    logger.info(f"Starting BMI calculation - Height: {height}m, Weight: {weight}kg")
    
    try:
        # Validate inputs
        if height is None or weight is None:
            logger.error("Height or weight is None")
            return None
        
        if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
            logger.error(f"Invalid input types - Height: {type(height)}, Weight: {type(weight)}")
            return None
        
        logger.info(f"Input validation passed - Height: {height}m, Weight: {weight}kg")
        
        # Calculate height squared
        height_squared = height ** 2
        logger.info(f"Height squared: {height_squared}")
        
        # Check for division by zero
        if height_squared == 0:
            logger.error("Height squared is zero - cannot calculate BMI")
            return None
        
        # Calculate BMI
        bmi = weight / height_squared
        logger.info(f"Raw BMI calculation: {weight} / {height_squared} = {bmi}")
        
        # Round to 2 decimal places
        rounded_bmi = round(bmi, 2)
        logger.info(f"Rounded BMI: {rounded_bmi}")
        
        logger.info(f"BMI calculation completed successfully: {rounded_bmi}")
        return rounded_bmi
        
    except Exception as e:
        logger.error(f"Error calculating BMI: {str(e)}")
        return None
