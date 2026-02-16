"""
Example script demonstrating the Intelligent Image Narration System.

This script shows how to use the system programmatically.
"""

from image_captioning import ImageCaptioner
from text_to_speech import TextToSpeech
from narrate import ImageNarrationSystem


def example_basic_usage():
    """Example: Basic usage of the narration system."""
    print("Example 1: Basic Usage")
    print("-" * 60)
    
    # Initialize the system
    system = ImageNarrationSystem()
    
    # Process an image (you'll need to provide an actual image path)
    # caption, audio_path = system.narrate_image("your_image.jpg")
    # print(f"Caption: {caption}")
    # print(f"Audio saved to: {audio_path}")
    
    print("System initialized successfully!")
    print("To use: system.narrate_image('path/to/image.jpg')")


def example_individual_components():
    """Example: Using individual components separately."""
    print("\n\nExample 2: Using Individual Components")
    print("-" * 60)
    
    # Image captioning only
    print("\n1. Image Captioning Component:")
    captioner = ImageCaptioner()
    # caption = captioner.generate_caption("your_image.jpg")
    # print(f"Caption: {caption}")
    print("Captioner initialized!")
    
    # Text-to-speech only
    print("\n2. Text-to-Speech Component:")
    tts = TextToSpeech()
    # audio_path = tts.text_to_speech("Hello, world!", "output/test.mp3")
    # print(f"Audio saved to: {audio_path}")
    print("TTS initialized!")


def example_custom_settings():
    """Example: Using custom settings."""
    print("\n\nExample 3: Custom Settings")
    print("-" * 60)
    
    # Custom TTS settings
    tts_slow = TextToSpeech(language='en', slow=True)
    print("TTS with slow speech initialized!")
    
    # Custom output locations
    # system = ImageNarrationSystem()
    # caption, audio = system.narrate_image(
    #     "image.jpg", 
    #     output_dir="custom_output",
    #     audio_filename="custom_name.mp3"
    # )


if __name__ == "__main__":
    print("="*60)
    print("Intelligent Image Narration System - Examples")
    print("="*60)
    
    # Run examples
    example_basic_usage()
    example_individual_components()
    example_custom_settings()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)
    print("\nNote: Uncomment the actual processing lines and provide")
    print("real image paths to see the system in action.")
