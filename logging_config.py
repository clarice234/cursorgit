"""
Centralized logging configuration for Cursor AI Training Code Examples.
Provides consistent logging setup across all sessions.
"""

import logging
import os
from datetime import datetime

def setup_logging(session_name, log_level=logging.INFO):
    """
    Set up logging configuration for a specific session.
    
    Args:
        session_name (str): Name of the session (e.g., 'Session_1_CoreUsage')
        log_level: Logging level (default: logging.INFO)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create session-specific log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{session_name}_{timestamp}.log"
    log_filepath = os.path.join(logs_dir, log_filename)
    
    # Configure logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ],
        force=True  # Override any existing configuration
    )
    
    logger = logging.getLogger(session_name)
    logger.info(f"Logging initialized for {session_name}")
    logger.info(f"Log file: {log_filepath}")
    
    return logger

def get_logger(name):
    """
    Get a logger instance with the specified name.
    
    Args:
        name (str): Logger name
    
    Returns:
        logging.Logger: Logger instance
    """
    return logging.getLogger(name)

def log_function_call(logger, func_name, args, kwargs=None):
    """
    Log function call with parameters.
    
    Args:
        logger: Logger instance
        func_name (str): Name of the function being called
        args: Function arguments
        kwargs: Function keyword arguments
    """
    if kwargs is None:
        kwargs = {}
    
    logger.info(f"Calling {func_name} with args: {args}, kwargs: {kwargs}")

def log_function_result(logger, func_name, result):
    """
    Log function result.
    
    Args:
        logger: Logger instance
        func_name (str): Name of the function
        result: Function return value
    """
    logger.info(f"{func_name} returned: {result}")

def log_error(logger, func_name, error, context=None):
    """
    Log error with context.
    
    Args:
        logger: Logger instance
        func_name (str): Name of the function where error occurred
        error: Error object or message
        context: Additional context information
    """
    logger.error(f"Error in {func_name}: {error}")
    if context:
        logger.error(f"Context: {context}")

def log_performance(logger, func_name, start_time, end_time):
    """
    Log function performance metrics.
    
    Args:
        logger: Logger instance
        func_name (str): Name of the function
        start_time: Start time (datetime or timestamp)
        end_time: End time (datetime or timestamp)
    """
    duration = end_time - start_time
    logger.info(f"{func_name} execution time: {duration.total_seconds():.4f} seconds")

# Example usage decorator
def log_function(logger):
    """
    Decorator to automatically log function calls and results.
    
    Args:
        logger: Logger instance to use for logging
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_function_call(logger, func.__name__, args, kwargs)
            try:
                result = func(*args, **kwargs)
                log_function_result(logger, func.__name__, result)
                return result
            except Exception as e:
                log_error(logger, func.__name__, e)
                raise
        return wrapper
    return decorator 