#!/usr/bin/env python3
"""
Demonstration script showing logging functionality across all sessions.
This script runs examples from each session and shows the logging output.
"""

import sys
import os
import time
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def demo_session_1():
    """Demonstrate logging in Session 1: Core Usage"""
    print("\n" + "="*60)
    print("SESSION 1: Core Usage - Discount Calculation")
    print("="*60)
    
    from Session_1_CoreUsage.example import get_discounted_price
    
    # Test cases with logging
    test_cases = [
        (100, 20),    # Normal case
        (50, 0),      # Zero discount
        (-10, 15),    # Negative price
        (200, 150),   # Over 100% discount
    ]
    
    for price, discount in test_cases:
        print(f"\n--- Testing: Price=${price}, Discount={discount}% ---")
        result = get_discounted_price(price, discount)
        print(f"Result: ${result}")

def demo_session_2():
    """Demonstrate logging in Session 2: Intermediate Skills"""
    print("\n" + "="*60)
    print("SESSION 2: Intermediate Skills - Palindrome Detection")
    print("="*60)
    
    from Session_2_Intermediate.palindrome import is_palindrome
    
    # Test cases with logging
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "12321",
        "",
        "Madam, I'm Adam.",
    ]
    
    for test_string in test_cases:
        print(f"\n--- Testing: '{test_string}' ---")
        result = is_palindrome(test_string)
        print(f"Result: {result}")

def demo_session_3():
    """Demonstrate logging in Session 3: Advanced Techniques"""
    print("\n" + "="*60)
    print("SESSION 3: Advanced Techniques - BMI Calculation")
    print("="*60)
    
    from Session_3_Advanced.utils import calculate_bmi
    
    # Test cases with logging
    test_cases = [
        (1.75, 70),   # Normal case
        (0, 70),      # Zero height
        (1.70, -50),  # Negative weight
        ("invalid", 70),  # Invalid input
    ]
    
    for height, weight in test_cases:
        print(f"\n--- Testing: Height={height}m, Weight={weight}kg ---")
        result = calculate_bmi(height, weight)
        print(f"Result: {result}")

def demo_session_4():
    """Demonstrate logging in Session 4: Debugging"""
    print("\n" + "="*60)
    print("SESSION 4: Debugging - Buggy Max Function")
    print("="*60)
    
    from Session_4_Debugging.buggy_max import find_max
    
    # Test cases with logging
    test_cases = [
        [1, 5, 3, 9, 2],      # Normal case
        [-5, -2, -10, -1],    # All negative (reveals bug)
        [],                    # Empty list (reveals bug)
        [42],                  # Single element
    ]
    
    for numbers in test_cases:
        print(f"\n--- Testing: {numbers} ---")
        result = find_max(numbers)
        print(f"Result: {result}")
        
        # Show what the correct result should be
        if numbers:
            correct_result = max(numbers)
            if result != correct_result:
                print(f"BUG DETECTED! Expected: {correct_result}, Got: {result}")

def demo_flask_app():
    """Demonstrate logging in Flask application"""
    print("\n" + "="*60)
    print("SESSION 3: Flask Application - BMI API")
    print("="*60)
    
    print("To test the Flask app with logging:")
    print("1. Navigate to Session_3_Advanced directory")
    print("2. Run: python app.py")
    print("3. Send POST request to http://localhost:5000/bmi")
    print("4. Check flask_app.log for detailed logging")

def main():
    """Run all logging demonstrations"""
    print("🧪 Cursor AI Training Code - Logging Demonstration")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        demo_session_1()
        demo_session_2()
        demo_session_3()
        demo_session_4()
        demo_flask_app()
        
        print("\n" + "="*60)
        print("✅ LOGGING DEMONSTRATION COMPLETED")
        print("="*60)
        print("\nLog files created:")
        print("- Session_1_CoreUsage: discount_calculation.log")
        print("- Session_2_Intermediate: palindrome_detection.log")
        print("- Session_3_Advanced: bmi_calculation.log, flask_app.log")
        print("- Session_4_Debugging: buggy_max.log")
        print("\nCheck these log files for detailed execution traces!")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 