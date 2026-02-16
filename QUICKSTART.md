# Quick Start Guide

This guide will help you get started with the Intelligent Image Narration System quickly.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dilip233/IntelligentImageNarration.git
   cd IntelligentImageNarration
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Test

Run the demo script to verify installation:
```bash
python demo.py
```

This will:
- Create a sample image
- Analyze it using the image narrator
- Generate an audio narration (requires internet)

## Running the Web Application

### Option 1: Using the run script (recommended)
```bash
python run.py
```

### Option 2: Direct Flask execution
```bash
python src/app.py
```

Then open your browser to: http://localhost:5000

## Using the System

1. **Upload an Image:**
   - Click "Choose Image File" button
   - Select an image file (PNG, JPG, JPEG, GIF, BMP, or WEBP)
   - Preview will appear

2. **Generate Narration:**
   - Click "Generate Narration" button
   - Wait for processing (first request takes longer)

3. **View Results:**
   - Read the generated text description
   - Listen to the audio narration (auto-plays)
   - Use "Replay Audio" to hear it again

4. **Upload Another Image:**
   - Click "Upload New Image" to start over

## Keyboard Shortcuts

- **Alt + N**: Upload a new image
- **Alt + R**: Replay audio narration

## Accessibility Features

The system is designed with accessibility in mind:

- ♿ Full keyboard navigation support
- 🔊 Screen reader compatible with ARIA labels
- 🎨 High contrast mode support
- 📱 Responsive design for all devices
- ⌨️ Keyboard shortcuts for common actions

## Programmatic Usage

You can also use the image narrator in your Python code:

```python
from src.image_narrator import ImageNarrator

# Initialize narrator
narrator = ImageNarrator()

# Analyze an image
caption = narrator.analyze_image('path/to/image.jpg')
print(f"Caption: {caption}")

# Generate audio narration
audio_path = narrator.generate_audio(caption, 'output.mp3')
print(f"Audio saved to: {audio_path}")

# Or do both in one step
result = narrator.narrate_image('path/to/image.jpg', 'output.mp3')
print(f"Caption: {result['caption']}")
print(f"Audio: {result['audio_path']}")
```

## Troubleshooting

### Model Loading Issues

If you see warnings about the transformers library:
```bash
pip install transformers torch
```

Note: The system will work with a fallback mode that provides basic image information even without the AI model.

### Audio Generation Fails

Audio generation requires an active internet connection. Ensure you're connected to the internet.

### Port Already in Use

If port 5000 is already in use, you can change it:
```python
# In src/app.py or run.py, modify:
app.run(debug=True, host='0.0.0.0', port=8000)  # Use port 8000 instead
```

## Testing

Run the test suite:
```bash
python -m unittest discover tests
```

## Getting Help

- Check the [README.md](README.md) for detailed information
- Review the [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Open an issue on GitHub for bugs or feature requests

## Next Steps

- Explore the [API documentation](README.md#api-endpoints)
- Try different types of images
- Contribute to the project!

Happy narrating! 🎉
