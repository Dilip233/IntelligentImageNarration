# Intelligent Image Narration System

An accessible image-to-speech system that generates audio narrations from images to support visually impaired users.

## Overview

This system uses state-of-the-art AI models to:
1. **Analyze images** - Generate descriptive captions using the BLIP (Bootstrapping Language-Image Pre-training) model
2. **Create audio narrations** - Convert captions to natural speech using Google Text-to-Speech

## Features

- 🖼️ Automatic image captioning using pre-trained AI models
- 🔊 Text-to-speech conversion for accessibility
- 📁 Batch processing support for multiple images
- 🎯 Simple command-line interface
- 🚀 Easy to use and extend

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Dilip233/IntelligentImageNarration.git
cd IntelligentImageNarration
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Narrate a single image:
```bash
python narrate.py path/to/image.jpg
```

### Multiple Images

Process multiple images at once:
```bash
python narrate.py image1.jpg image2.jpg image3.jpg
```

### Custom Output Directory

Specify where to save audio files:
```bash
python narrate.py image.jpg --output-dir my_narrations
```

### Output

The system will:
- Generate a descriptive caption for each image
- Create an MP3 audio file with the narration
- Save audio files to the `output/` directory (or specified directory)

## Example

```bash
$ python narrate.py sunset.jpg

Initializing Intelligent Image Narration System...
Loading image captioning model: Salesforce/blip-image-captioning-base
Model loaded successfully on cpu
System initialized successfully!

Processing image: sunset.jpg
Generating image caption...
Caption: a beautiful sunset over the ocean with orange and pink sky

Converting caption to speech...
Audio narration saved to: output/sunset_narration.mp3

============================================================
SUCCESS!
============================================================
Caption: a beautiful sunset over the ocean with orange and pink sky
Audio: output/sunset_narration.mp3
```

## System Architecture

```
┌─────────────────┐
│  Input Image    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Image Captioning       │
│  (BLIP Model)           │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Generated Caption      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Text-to-Speech         │
│  (gTTS)                 │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Audio Narration (MP3)  │
└─────────────────────────┘
```

## Components

### 1. Image Captioning (`image_captioning.py`)
- Uses BLIP (Salesforce/blip-image-captioning-base) model
- Generates natural language descriptions of images
- Supports GPU acceleration when available

### 2. Text-to-Speech (`text_to_speech.py`)
- Converts text captions to audio using Google TTS
- Generates MP3 audio files
- Supports multiple languages

### 3. Main Application (`narrate.py`)
- CLI interface for the system
- Handles single and batch image processing
- Manages the workflow between components

## Requirements

- Python 3.8+
- PyTorch
- Transformers (Hugging Face)
- Pillow
- gTTS (Google Text-to-Speech)

See `requirements.txt` for detailed version information.

## Use Cases

- **Accessibility**: Help visually impaired users understand image content
- **Education**: Create audio descriptions for educational materials
- **Social Media**: Generate audio descriptions for images in posts
- **Documentation**: Add audio narrations to visual documentation
- **Content Creation**: Automate image description for multimedia content

## Future Enhancements

- Support for multiple languages
- More detailed captioning options
- Integration with screen readers
- Real-time processing
- Web interface
- API endpoint support

## License

This project is open source and available for educational and accessibility purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- BLIP model by Salesforce Research
- gTTS library for text-to-speech conversion
- Hugging Face Transformers library
