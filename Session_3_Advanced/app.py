from flask import Flask, request, jsonify
from utils import calculate_bmi
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('flask_app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi_route():
    """
    Calculate BMI via HTTP POST request.
    
    Expected JSON payload:
    {
        "height": float,  // Height in meters
        "weight": float   // Weight in kilograms
    }
    
    Returns:
        JSON response with calculated BMI
    """
    logger.info("Received BMI calculation request")
    
    try:
        # Get JSON data from request
        data = request.get_json()
        logger.info(f"Request data: {data}")
        
        if data is None:
            logger.warning("No JSON data provided in request")
            return jsonify({"bmi": None}), 400
        
        # Extract height and weight from request
        height = data.get("height")
        weight = data.get("weight")
        
        logger.info(f"Extracted values - Height: {height}, Weight: {weight}")
        
        # Check if both values are provided
        if height is None or weight is None:
            logger.warning(f"Missing required data - Height: {height}, Weight: {weight}")
            return jsonify({"bmi": None}), 400
        
        # Calculate BMI
        logger.info("Calling BMI calculation function")
        bmi_result = calculate_bmi(height, weight)
        logger.info(f"BMI calculation result: {bmi_result}")
        
        # Prepare response
        response_data = {"bmi": bmi_result}
        logger.info(f"Preparing response: {response_data}")
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Error processing BMI request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    logger.warning(f"405 error: {request.method} {request.url}")
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    logger.info("Starting Flask BMI application")
    app.run(debug=True)
