#!/usr/bin/env python3
"""
Master test runner for Cursor AI Training Code Examples.
Runs all unit tests across all sessions and provides a comprehensive report.
"""

import unittest
import sys
import os
from pathlib import Path

def run_session_tests(session_path, session_name):
    """Run all tests in a specific session directory."""
    print(f"\n{'='*60}")
    print(f"Running tests for {session_name}")
    print(f"{'='*60}")
    
    # Change to session directory
    original_dir = os.getcwd()
    os.chdir(session_path)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return to original directory
    os.chdir(original_dir)
    
    return result

def main():
    """Main function to run all tests."""
    print("🧪 Cursor AI Training Code - Test Suite")
    print("=" * 60)
    
    # Define sessions
    sessions = [
        ("Session_1_CoreUsage", "Session 1: Core Usage"),
        ("Session_2_Intermediate", "Session 2: Intermediate Skills"),
        ("Session_3_Advanced", "Session 3: Advanced Techniques"),
        ("Session_4_Debugging", "Session 4: Debugging")
    ]
    
    total_tests = 0
    total_failures = 0
    total_errors = 0
    
    # Run tests for each session
    for session_path, session_name in sessions:
        if os.path.exists(session_path):
            result = run_session_tests(session_path, session_name)
            total_tests += result.testsRun
            total_failures += len(result.failures)
            total_errors += len(result.errors)
        else:
            print(f"\n❌ Session directory not found: {session_path}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total tests run: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Errors: {total_errors}")
    print(f"Success rate: {((total_tests - total_failures - total_errors) / total_tests * 100):.1f}%" if total_tests > 0 else "No tests run")
    
    # Note about expected failures in Session 4
    if total_failures > 0:
        print(f"\n💡 Note: Some failures in Session 4 are expected!")
        print("   The buggy_max.py function has intentional bugs for debugging practice.")
        print("   These failures help identify the bugs that need to be fixed.")
    
    return total_failures + total_errors == 0

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1) 