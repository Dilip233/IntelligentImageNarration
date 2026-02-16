# Intelligent Image Narration System

An accessibility-focused system that analyzes images using AI and provides audio narration to help visually impaired users understand visual content.

## Features

- 🖼️ **AI-Powered Image Analysis**: Uses state-of-the-art BLIP model to generate descriptive captions
- 🔊 **Text-to-Speech Narration**: Converts image descriptions to natural-sounding audio
- ♿ **Accessibility First**: Built with WCAG 2.1 guidelines in mind
  - Full keyboard navigation support (Alt+N for new image, Alt+R to replay)
  - ARIA labels and landmarks for screen readers
  - High contrast mode support
  - Semantic HTML structure
- 🌐 **Web Interface**: Easy-to-use responsive web application
- 🚀 **Fast Processing**: Efficient image analysis and audio generation
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Python, Flask
- **AI/ML**: Transformers (BLIP model), PyTorch
- **Image Processing**: Pillow, OpenCV
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Dilip233/IntelligentImageNarration.git
cd IntelligentImageNarration
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. Start the Flask server:
```bash
python src/app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload an image and receive:
   - A descriptive text caption
   - An audio narration that automatically plays

### Using the Image Narrator Module

You can also use the image narrator programmatically:

```python
from src.image_narrator import ImageNarrator

# Initialize narrator
narrator = ImageNarrator()

# Analyze an image and generate audio
result = narrator.narrate_image(
    image_path='path/to/image.jpg',
    audio_output_path='output/narration.mp3'
)

print(f"Caption: {result['caption']}")
print(f"Audio saved to: {result['audio_path']}")
```

## Accessibility Features

### Keyboard Shortcuts
- **Alt + N**: Upload a new image
- **Alt + R**: Replay audio narration

### Screen Reader Support
- All interactive elements have proper ARIA labels
- Dynamic content changes are announced
- Semantic HTML structure for easy navigation

### Visual Accessibility
- High contrast color scheme
- Clear focus indicators
- Responsive text sizing
- Support for browser zoom

## Project Structure

```
IntelligentImageNarration/
├── src/
│   ├── app.py              # Flask web application
│   └── image_narrator.py   # Core image narration logic
├── templates/
│   └── index.html          # Main web interface
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet
│   ├── js/
│   │   └── main.js         # Frontend JavaScript
│   └── audio/              # Generated audio files
├── tests/
│   ├── test_app.py         # Flask app tests
│   └── test_image_narrator.py  # Image narrator tests
├── uploads/                # Temporary image uploads
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Testing

Run the test suite:

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests/test_image_narrator.py
python -m unittest tests/test_app.py
```

Note: Some tests may be skipped if the AI model cannot be loaded in the test environment.

## API Endpoints

### GET /
Returns the main web interface.

### POST /upload
Upload an image for narration.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `image` (file)

**Response:**
```json
{
  "success": true,
  "caption": "A description of the image",
  "audio_url": "/static/audio/narration.mp3"
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)

Maximum file size: 16MB

## Performance Considerations

- **First Request**: May take longer as the AI model needs to be loaded into memory
- **Subsequent Requests**: Much faster as the model remains in memory
- **Model Size**: BLIP model is approximately 1GB and requires adequate RAM

## Limitations

- Requires internet connection for text-to-speech generation (gTTS)
- Model performance depends on image quality and content
- Audio files are generated on-demand and stored temporarily

## Future Enhancements

- [ ] Support for multiple languages
- [ ] Offline text-to-speech capability
- [ ] Batch processing of multiple images
- [ ] Custom voice options
- [ ] More detailed image descriptions
- [ ] Integration with cloud storage services
- [ ] Mobile app version

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- BLIP model by Salesforce Research
- gTTS for text-to-speech functionality
- The accessibility community for guidelines and best practices

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/Dilip233/IntelligentImageNarration).
