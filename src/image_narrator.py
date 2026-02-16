"""
Intelligent Image Narration System
A system that analyzes images and provides audio narration for accessibility support
"""

import os
import logging
from PIL import Image
from gtts import gTTS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImageNarrator:
    """Main class for image narration functionality"""
    
    def __init__(self):
        """Initialize the image narrator with AI model"""
        logger.info("Initializing Image Narrator...")
        self.processor = None
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Lazy load the AI model"""
        try:
            # Import transformers here to allow the module to be imported without it
            from transformers import BlipProcessor, BlipForConditionalGeneration
            
            # Load BLIP model for image captioning
            self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
            self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
            logger.info("Model loaded successfully")
        except ImportError as e:
            logger.warning(f"Transformers library not available: {e}")
            logger.warning("Image narration will use fallback description")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            logger.warning("Image narration will use fallback description")
    
    def analyze_image(self, image_path):
        """
        Analyze an image and generate a descriptive caption
        
        Args:
            image_path: Path to the image file
            
        Returns:
            str: Generated caption describing the image
        """
        try:
            # Load and process image
            image = Image.open(image_path).convert('RGB')
            
            # Check if model is available
            if self.model is None or self.processor is None:
                # Fallback: provide a basic description based on image properties
                width, height = image.size
                mode = image.mode
                caption = f"An image with dimensions {width}x{height} in {mode} color mode."
                logger.info(f"Using fallback caption: {caption}")
                return caption
            
            # Generate caption using AI model
            inputs = self.processor(image, return_tensors="pt")
            out = self.model.generate(**inputs, max_length=50)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            
            logger.info(f"Generated caption: {caption}")
            return caption
        except Exception as e:
            logger.error(f"Error analyzing image: {e}")
            raise
    
    def generate_audio(self, text, output_path):
        """
        Convert text to speech and save as audio file
        
        Args:
            text: Text to convert to speech
            output_path: Path where audio file should be saved
            
        Returns:
            str: Path to the generated audio file
        """
        try:
            # Generate speech
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(output_path)
            
            logger.info(f"Audio generated: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error generating audio: {e}")
            raise
    
    def narrate_image(self, image_path, audio_output_path):
        """
        Complete workflow: analyze image and generate audio narration
        
        Args:
            image_path: Path to the image file
            audio_output_path: Path where audio file should be saved
            
        Returns:
            dict: Contains caption text and audio file path
        """
        try:
            # Analyze image
            caption = self.analyze_image(image_path)
            
            # Generate audio narration
            audio_path = self.generate_audio(caption, audio_output_path)
            
            return {
                'caption': caption,
                'audio_path': audio_path
            }
        except Exception as e:
            logger.error(f"Error in narration workflow: {e}")
            raise


def main():
    """Main function for testing"""
    narrator = ImageNarrator()
    print("Image Narrator initialized successfully!")


if __name__ == "__main__":
    main()
