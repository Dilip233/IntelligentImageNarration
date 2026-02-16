"""
Flask web application for Intelligent Image Narration System
"""

import os
import uuid
import threading
from flask import Flask, render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from src.image_narrator import ImageNarrator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

# Configuration
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'static/audio'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# Initialize narrator (lazy loading with thread safety)
narrator = None
narrator_lock = threading.Lock()


def get_narrator():
    """Thread-safe lazy load the narrator to avoid loading model on startup"""
    global narrator
    if narrator is None:
        with narrator_lock:
            # Double-check locking pattern
            if narrator is None:
                narrator = ImageNarrator()
    return narrator


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload and generate narration"""
    try:
        # Check if image file is present
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check if file type is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed types: ' + ', '.join(ALLOWED_EXTENSIONS)}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        logger.info(f"Image uploaded: {filepath}")
        
        # Generate audio narration
        audio_filename = f"{uuid.uuid4()}.mp3"
        audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
        
        # Get narrator and process image
        img_narrator = get_narrator()
        result = img_narrator.narrate_image(filepath, audio_path)
        
        # Clean up uploaded image
        os.remove(filepath)
        
        # Return result
        return jsonify({
            'success': True,
            'caption': result['caption'],
            'audio_url': url_for('static', filename=f'audio/{audio_filename}')
        })
        
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    # Note: Debug mode is enabled for development only
    # In production, use a proper WSGI server like Gunicorn or uWSGI
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 src.app:app
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
