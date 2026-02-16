"""
Intelligent Image Narration System
Main application for generating audio narrations from images for accessibility support.
"""

import argparse
import os
import sys
from image_captioning import ImageCaptioner
from text_to_speech import TextToSpeech


class ImageNarrationSystem:
    """
    Main system that combines image captioning and text-to-speech
    to provide audio narrations for images.
    """
    
    def __init__(self):
        """Initialize the image narration system."""
        print("Initializing Intelligent Image Narration System...")
        self.captioner = ImageCaptioner()
        self.tts = TextToSpeech()
        print("System initialized successfully!\n")
    
    def narrate_image(self, image_path, output_dir="output", audio_filename=None):
        """
        Generate audio narration for an image.
        
        Args:
            image_path (str): Path to the input image
            output_dir (str): Directory to save the audio file
            audio_filename (str): Name for the output audio file (optional)
            
        Returns:
            tuple: (caption, audio_path) - Generated caption and path to audio file
        """
        print(f"Processing image: {image_path}")
        
        # Validate image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Generate caption
        print("Generating image caption...")
        caption = self.captioner.generate_caption(image_path)
        print(f"Caption: {caption}\n")
        
        # Generate audio filename if not provided
        if audio_filename is None:
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            audio_filename = f"{base_name}_narration.mp3"
        
        # Convert caption to speech
        print("Converting caption to speech...")
        audio_path = self.tts.narrate_caption(caption, output_dir, audio_filename)
        
        return caption, audio_path
    
    def narrate_multiple_images(self, image_paths, output_dir="output"):
        """
        Generate audio narrations for multiple images.
        
        Args:
            image_paths (list): List of paths to input images
            output_dir (str): Directory to save the audio files
            
        Returns:
            list: List of tuples (image_path, caption, audio_path)
        """
        results = []
        
        for i, image_path in enumerate(image_paths, 1):
            print(f"\n{'='*60}")
            print(f"Processing image {i}/{len(image_paths)}")
            print(f"{'='*60}")
            
            try:
                caption, audio_path = self.narrate_image(image_path, output_dir)
                results.append((image_path, caption, audio_path))
            except Exception as e:
                print(f"Error processing {image_path}: {str(e)}")
                results.append((image_path, None, None))
        
        return results


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Intelligent Image Narration System for Accessibility Support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Narrate a single image
  python narrate.py image.jpg
  
  # Narrate multiple images
  python narrate.py image1.jpg image2.jpg image3.jpg
  
  # Specify output directory
  python narrate.py image.jpg --output-dir my_output
        """
    )
    
    parser.add_argument(
        'images',
        nargs='+',
        help='Path(s) to image file(s) to narrate'
    )
    
    parser.add_argument(
        '--output-dir',
        default='output',
        help='Directory to save audio narrations (default: output)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize the system
        system = ImageNarrationSystem()
        
        # Process images
        if len(args.images) == 1:
            caption, audio_path = system.narrate_image(args.images[0], args.output_dir)
            print(f"\n{'='*60}")
            print("SUCCESS!")
            print(f"{'='*60}")
            print(f"Caption: {caption}")
            print(f"Audio: {audio_path}")
        else:
            results = system.narrate_multiple_images(args.images, args.output_dir)
            
            print(f"\n{'='*60}")
            print("SUMMARY")
            print(f"{'='*60}")
            
            successful = sum(1 for _, caption, _ in results if caption is not None)
            print(f"Successfully processed: {successful}/{len(results)} images\n")
            
            for image_path, caption, audio_path in results:
                if caption:
                    print(f"✓ {image_path}")
                    print(f"  Caption: {caption}")
                    print(f"  Audio: {audio_path}\n")
                else:
                    print(f"✗ {image_path} - Failed\n")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
