"""
Image Captioning Module
Uses a pre-trained image captioning model to generate descriptions for images.
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch


class ImageCaptioner:
    """
    A class to generate captions for images using the BLIP model.
    """
    
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        """
        Initialize the image captioning model.
        
        Args:
            model_name (str): The name of the pre-trained model to use
        """
        print(f"Loading image captioning model: {model_name}")
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        
        # Use GPU if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        print(f"Model loaded successfully on {self.device}")
    
    def generate_caption(self, image_path, max_length=50):
        """
        Generate a caption for the given image.
        
        Args:
            image_path (str): Path to the image file
            max_length (int): Maximum length of the generated caption
            
        Returns:
            str: Generated caption for the image
        """
        try:
            # Load and process the image
            image = Image.open(image_path).convert('RGB')
            
            # Process the image
            inputs = self.processor(image, return_tensors="pt").to(self.device)
            
            # Generate caption
            outputs = self.model.generate(**inputs, max_length=max_length)
            
            # Decode the generated caption
            caption = self.processor.decode(outputs[0], skip_special_tokens=True)
            
            return caption
            
        except Exception as e:
            raise Exception(f"Error generating caption: {str(e)}")
