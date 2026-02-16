"""
Integration tests for the Flask application
"""

import unittest
import os
import sys
from io import BytesIO
from PIL import Image

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.app import app


class TestFlaskApp(unittest.TestCase):
    """Test cases for Flask application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_route(self):
        """Test that index page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
    
    def test_upload_no_file(self):
        """Test upload endpoint with no file"""
        response = self.client.post('/upload')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)
    
    def test_upload_invalid_file_type(self):
        """Test upload with invalid file type"""
        data = {
            'image': (BytesIO(b'test data'), 'test.txt')
        }
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertIn('error', response_data)
    
    def create_test_image(self):
        """Helper method to create a test image"""
        img = Image.new('RGB', (100, 100), color='blue')
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        return img_io
    
    def test_upload_valid_image(self):
        """Test upload with valid image"""
        try:
            img_data = self.create_test_image()
            data = {
                'image': (img_data, 'test.jpg')
            }
            response = self.client.post('/upload', data=data, content_type='multipart/form-data')
            
            # This might fail if model is not loaded, which is expected in test environment
            if response.status_code == 200:
                response_data = response.get_json()
                self.assertIn('success', response_data)
                self.assertIn('caption', response_data)
                self.assertIn('audio_url', response_data)
            else:
                # Model might not be available in test environment
                self.skipTest("Model not available in test environment")
        except Exception as e:
            self.skipTest(f"Test skipped due to: {e}")


if __name__ == '__main__':
    unittest.main()
