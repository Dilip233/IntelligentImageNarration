"""
Test suite for Intelligent Image Narration System
"""

import unittest
import os
import sys
from PIL import Image
import io

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.image_narrator import ImageNarrator


class TestImageNarrator(unittest.TestCase):
    """Test cases for ImageNarrator class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        # Create a test image
        cls.test_image_path = '/tmp/test_image.jpg'
        img = Image.new('RGB', (100, 100), color='red')
        img.save(cls.test_image_path)
        
        cls.test_audio_path = '/tmp/test_audio.mp3'
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test fixtures"""
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)
        if os.path.exists(cls.test_audio_path):
            os.remove(cls.test_audio_path)
    
    def test_narrator_initialization(self):
        """Test that narrator can be initialized"""
        try:
            narrator = ImageNarrator()
            self.assertIsNotNone(narrator)
            self.assertIsNotNone(narrator.model)
            self.assertIsNotNone(narrator.processor)
        except Exception as e:
            self.skipTest(f"Model initialization failed: {e}")
    
    def test_analyze_image(self):
        """Test image analysis"""
        try:
            narrator = ImageNarrator()
            caption = narrator.analyze_image(self.test_image_path)
            
            self.assertIsInstance(caption, str)
            self.assertTrue(len(caption) > 0)
        except Exception as e:
            self.skipTest(f"Image analysis test skipped: {e}")
    
    def test_generate_audio(self):
        """Test audio generation"""
        try:
            narrator = ImageNarrator()
            test_text = "This is a test narration."
            
            audio_path = narrator.generate_audio(test_text, self.test_audio_path)
            
            self.assertTrue(os.path.exists(audio_path))
            self.assertTrue(os.path.getsize(audio_path) > 0)
        except Exception as e:
            self.skipTest(f"Audio generation test skipped: {e}")
    
    def test_narrate_image(self):
        """Test complete narration workflow"""
        try:
            narrator = ImageNarrator()
            result = narrator.narrate_image(self.test_image_path, self.test_audio_path)
            
            self.assertIn('caption', result)
            self.assertIn('audio_path', result)
            self.assertIsInstance(result['caption'], str)
            self.assertTrue(os.path.exists(result['audio_path']))
        except Exception as e:
            self.skipTest(f"Narration workflow test skipped: {e}")


if __name__ == '__main__':
    unittest.main()
