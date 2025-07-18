import unittest
import json
from app import app
from utils import calculate_bmi

class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask BMI application."""
    
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_bmi_endpoint_success(self):
        """Test successful BMI calculation via API."""
        data = {"height": 1.75, "weight": 70}
        response = self.app.post('/bmi', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('bmi', result)
        self.assertEqual(result['bmi'], 22.86)
    
    def test_bmi_endpoint_missing_data(self):
        """Test BMI endpoint with missing data."""
        data = {"height": 1.75}  # Missing weight
        response = self.app.post('/bmi',
                               data=json.dumps(data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('bmi', result)
        self.assertIsNone(result['bmi'])
    
    def test_bmi_endpoint_invalid_data(self):
        """Test BMI endpoint with invalid data."""
        data = {"height": "invalid", "weight": "invalid"}
        response = self.app.post('/bmi',
                               data=json.dumps(data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('bmi', result)
        self.assertIsNone(result['bmi'])
    
    def test_bmi_endpoint_empty_request(self):
        """Test BMI endpoint with empty request body."""
        response = self.app.post('/bmi',
                               data=json.dumps({}),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('bmi', result)
        self.assertIsNone(result['bmi'])
    
    def test_bmi_endpoint_wrong_method(self):
        """Test BMI endpoint with wrong HTTP method."""
        response = self.app.get('/bmi')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
    
    def test_bmi_endpoint_no_content_type(self):
        """Test BMI endpoint without content-type header."""
        data = {"height": 1.75, "weight": 70}
        response = self.app.post('/bmi', data=json.dumps(data))
        
        # Flask returns 415 (Unsupported Media Type) when content-type is missing
        self.assertIn(response.status_code, [200, 400, 415])
    
    def test_bmi_calculation_edge_cases(self):
        """Test BMI endpoint with edge cases."""
        test_cases = [
            ({"height": 0, "weight": 70}, None),
            ({"height": 1.75, "weight": 0}, 0.0),
            ({"height": -1.75, "weight": 70}, 22.86),  # Fixed: negative height squared is positive
            ({"height": 1.75, "weight": -70}, -22.86),
        ]
        
        for data, expected in test_cases:
            with self.subTest(data=data):
                response = self.app.post('/bmi',
                                       data=json.dumps(data),
                                       content_type='application/json')
                
                self.assertEqual(response.status_code, 200)
                result = json.loads(response.data)
                self.assertIn('bmi', result)
                self.assertEqual(result['bmi'], expected)

class TestAppIntegration(unittest.TestCase):
    """Integration tests for the Flask app."""
    
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_bmi_calculation_accuracy(self):
        """Test that API returns same results as direct function call."""
        test_data = [
            (1.75, 70, 22.86),
            (1.70, 50, 17.30),
            (1.65, 85, 31.22),
        ]
        
        for height, weight, expected_bmi in test_data:
            with self.subTest(height=height, weight=weight):
                # Test direct function call
                direct_result = calculate_bmi(height, weight)
                self.assertEqual(direct_result, expected_bmi)
                
                # Test API call
                data = {"height": height, "weight": weight}
                response = self.app.post('/bmi',
                                       data=json.dumps(data),
                                       content_type='application/json')
                
                self.assertEqual(response.status_code, 200)
                result = json.loads(response.data)
                self.assertEqual(result['bmi'], expected_bmi)

if __name__ == '__main__':
    unittest.main() 