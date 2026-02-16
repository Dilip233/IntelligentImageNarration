#!/usr/bin/env python3
"""
Demo script to test the Intelligent Image Narration System
This creates a sample image and demonstrates the core functionality
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from image_narrator import ImageNarrator


def create_demo_image():
    """Create a simple demo image"""
    # Create a colorful demo image
    img = Image.new('RGB', (400, 300), color='skyblue')
    draw = ImageDraw.Draw(img)
    
    # Draw some shapes
    draw.rectangle([50, 50, 150, 150], fill='red', outline='black', width=3)
    draw.ellipse([200, 50, 350, 200], fill='yellow', outline='black', width=3)
    draw.polygon([(100, 200), (200, 150), (300, 200)], fill='green', outline='black')
    
    # Add text
    try:
        draw.text((150, 250), "Demo Image", fill='black')
    except:
        pass  # If font not available, skip text
    
    # Save image
    os.makedirs('demo', exist_ok=True)
    img_path = 'demo/demo_image.jpg'
    img.save(img_path)
    print(f"✓ Demo image created: {img_path}")
    return img_path


def main():
    """Run the demo"""
    print("=" * 60)
    print("Intelligent Image Narration System - Demo")
    print("=" * 60)
    print()
    
    # Create demo image
    print("Step 1: Creating demo image...")
    image_path = create_demo_image()
    print()
    
    # Initialize narrator
    print("Step 2: Initializing Image Narrator...")
    narrator = ImageNarrator()
    print()
    
    # Analyze image
    print("Step 3: Analyzing image...")
    try:
        caption = narrator.analyze_image(image_path)
        print(f"✓ Generated caption: '{caption}'")
        print()
        
        # Generate audio (might fail without internet)
        print("Step 4: Generating audio narration...")
        audio_path = 'demo/demo_narration.mp3'
        try:
            narrator.generate_audio(caption, audio_path)
            print(f"✓ Audio saved to: {audio_path}")
            print()
            print("Demo complete! Check the 'demo' folder for results.")
        except Exception as e:
            print(f"⚠ Audio generation failed (requires internet): {e}")
            print("Note: Audio narration requires an active internet connection.")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1
    
    print()
    print("=" * 60)
    print("To use the web interface, run: python run.py")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
