"""
Text-to-Speech Module
Converts text captions to audio narration for accessibility.
"""

from gtts import gTTS
import os


class TextToSpeech:
    """
    A class to convert text to speech audio.
    """
    
    def __init__(self, language='en', slow=False):
        """
        Initialize the text-to-speech converter.
        
        Args:
            language (str): Language code for speech synthesis (default: 'en')
            slow (bool): Whether to speak slowly (default: False)
        """
        self.language = language
        self.slow = slow
    
    def text_to_speech(self, text, output_path):
        """
        Convert text to speech and save as audio file.
        
        Args:
            text (str): Text to convert to speech
            output_path (str): Path where the audio file will be saved
            
        Returns:
            str: Path to the saved audio file
        """
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang=self.language, slow=self.slow)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            
            # Save the audio file
            tts.save(output_path)
            
            print(f"Audio narration saved to: {output_path}")
            return output_path
            
        except Exception as e:
            raise Exception(f"Error converting text to speech: {str(e)}")
    
    def narrate_caption(self, caption, output_dir="output", filename="narration.mp3"):
        """
        Convert an image caption to speech narration.
        
        Args:
            caption (str): Caption text to narrate
            output_dir (str): Directory to save the audio file
            filename (str): Name of the output audio file
            
        Returns:
            str: Path to the saved audio file
        """
        output_path = os.path.join(output_dir, filename)
        return self.text_to_speech(caption, output_path)
