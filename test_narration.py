"""
Unit tests for the Intelligent Image Narration System.

These tests verify the structure and basic functionality of the system components.
"""

import unittest
import os
import sys
from unittest.mock import Mock, patch, MagicMock


class TestImageCaptioning(unittest.TestCase):
    """Test cases for the ImageCaptioner class."""
    
    @patch('image_captioning.BlipProcessor')
    @patch('image_captioning.BlipForConditionalGeneration')
    def test_init_captioner(self, mock_model, mock_processor):
        """Test that ImageCaptioner initializes correctly."""
        from image_captioning import ImageCaptioner
        
        # Mock the model and processor
        mock_processor.from_pretrained.return_value = MagicMock()
        mock_model.from_pretrained.return_value = MagicMock()
        
        # Initialize captioner
        captioner = ImageCaptioner()
        
        # Verify initialization
        self.assertIsNotNone(captioner.processor)
        self.assertIsNotNone(captioner.model)
        mock_processor.from_pretrained.assert_called_once()
        mock_model.from_pretrained.assert_called_once()
    
    @patch('image_captioning.Image')
    @patch('image_captioning.BlipProcessor')
    @patch('image_captioning.BlipForConditionalGeneration')
    def test_generate_caption(self, mock_model_class, mock_processor_class, mock_image):
        """Test caption generation."""
        from image_captioning import ImageCaptioner
        
        # Setup mocks
        mock_processor = MagicMock()
        mock_model = MagicMock()
        mock_processor_class.from_pretrained.return_value = mock_processor
        mock_model_class.from_pretrained.return_value = mock_model
        
        # Mock image processing
        mock_image.open.return_value.convert.return_value = MagicMock()
        mock_processor.return_value.to.return_value = {"pixel_values": MagicMock()}
        mock_model.generate.return_value = [MagicMock()]
        mock_processor.decode.return_value = "a beautiful landscape"
        
        # Test caption generation
        captioner = ImageCaptioner()
        caption = captioner.generate_caption("test.jpg")
        
        # Verify
        self.assertEqual(caption, "a beautiful landscape")


class TestTextToSpeech(unittest.TestCase):
    """Test cases for the TextToSpeech class."""
    
    def test_init_tts(self):
        """Test that TextToSpeech initializes correctly."""
        from text_to_speech import TextToSpeech
        
        tts = TextToSpeech(language='en', slow=False)
        
        self.assertEqual(tts.language, 'en')
        self.assertEqual(tts.slow, False)
    
    @patch('text_to_speech.gTTS')
    @patch('text_to_speech.os.makedirs')
    def test_text_to_speech(self, mock_makedirs, mock_gtts):
        """Test text-to-speech conversion."""
        from text_to_speech import TextToSpeech
        
        # Mock gTTS
        mock_tts_instance = MagicMock()
        mock_gtts.return_value = mock_tts_instance
        
        # Test conversion
        tts = TextToSpeech()
        output_path = tts.text_to_speech("Hello world", "output/test.mp3")
        
        # Verify
        mock_gtts.assert_called_once_with(text="Hello world", lang='en', slow=False)
        mock_tts_instance.save.assert_called_once_with("output/test.mp3")
        self.assertEqual(output_path, "output/test.mp3")


class TestImageNarrationSystem(unittest.TestCase):
    """Test cases for the ImageNarrationSystem class."""
    
    @patch('narrate.ImageCaptioner')
    @patch('narrate.TextToSpeech')
    def test_init_system(self, mock_tts, mock_captioner):
        """Test that ImageNarrationSystem initializes correctly."""
        from narrate import ImageNarrationSystem
        
        # Initialize system
        system = ImageNarrationSystem()
        
        # Verify components are initialized
        self.assertIsNotNone(system.captioner)
        self.assertIsNotNone(system.tts)
    
    @patch('narrate.os.path.exists')
    @patch('narrate.ImageCaptioner')
    @patch('narrate.TextToSpeech')
    def test_narrate_image(self, mock_tts_class, mock_captioner_class, mock_exists):
        """Test image narration."""
        from narrate import ImageNarrationSystem
        
        # Setup mocks
        mock_captioner = MagicMock()
        mock_tts = MagicMock()
        mock_captioner_class.return_value = mock_captioner
        mock_tts_class.return_value = mock_tts
        mock_exists.return_value = True
        
        # Mock methods
        mock_captioner.generate_caption.return_value = "a test caption"
        mock_tts.narrate_caption.return_value = "output/test_narration.mp3"
        
        # Test narration
        system = ImageNarrationSystem()
        caption, audio_path = system.narrate_image("test.jpg")
        
        # Verify
        self.assertEqual(caption, "a test caption")
        self.assertEqual(audio_path, "output/test_narration.mp3")
        mock_captioner.generate_caption.assert_called_once_with("test.jpg")
        mock_tts.narrate_caption.assert_called_once()


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for the system."""
    
    def test_imports(self):
        """Test that all modules can be imported."""
        import image_captioning
        import text_to_speech
        import narrate
        
        self.assertTrue(hasattr(image_captioning, 'ImageCaptioner'))
        self.assertTrue(hasattr(text_to_speech, 'TextToSpeech'))
        self.assertTrue(hasattr(narrate, 'ImageNarrationSystem'))
    
    def test_class_structure(self):
        """Test that classes have required methods."""
        from image_captioning import ImageCaptioner
        from text_to_speech import TextToSpeech
        from narrate import ImageNarrationSystem
        
        # Check ImageCaptioner has required methods
        self.assertTrue(hasattr(ImageCaptioner, 'generate_caption'))
        
        # Check TextToSpeech has required methods
        self.assertTrue(hasattr(TextToSpeech, 'text_to_speech'))
        self.assertTrue(hasattr(TextToSpeech, 'narrate_caption'))
        
        # Check ImageNarrationSystem has required methods
        self.assertTrue(hasattr(ImageNarrationSystem, 'narrate_image'))
        self.assertTrue(hasattr(ImageNarrationSystem, 'narrate_multiple_images'))


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
