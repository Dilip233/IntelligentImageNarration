#!/usr/bin/env python3
"""
Quick start script for Intelligent Image Narration System
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import app

if __name__ == '__main__':
    print("=" * 60)
    print("Intelligent Image Narration System")
    print("=" * 60)
    print("\nStarting server in development mode...")
    print("Once started, open your browser to: http://localhost:5000")
    print("\nNote: First request may take longer as AI model loads.")
    print("Press Ctrl+C to stop the server.")
    print("\nIMPORTANT: For production, use a WSGI server like Gunicorn:")
    print("  gunicorn -w 4 -b 0.0.0.0:5000 src.app:app")
    print("=" * 60)
    
    # Enable debug mode for development
    os.environ['FLASK_DEBUG'] = 'true'
    app.run(debug=True, host='0.0.0.0', port=5000)
