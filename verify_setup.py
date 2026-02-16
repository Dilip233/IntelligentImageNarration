#!/usr/bin/env python3
"""
Setup verification script for Intelligent Image Narration System
This script checks if all dependencies are properly installed
"""

import sys
import importlib


def check_module(module_name, package_name=None):
    """Check if a module can be imported"""
    display_name = package_name or module_name
    try:
        importlib.import_module(module_name)
        print(f"✓ {display_name} is installed")
        return True
    except ImportError:
        print(f"✗ {display_name} is NOT installed")
        return False


def main():
    """Run all checks"""
    print("=" * 60)
    print("Intelligent Image Narration System - Setup Verification")
    print("=" * 60)
    print()
    
    print("Checking required dependencies...")
    print()
    
    required = [
        ("flask", "Flask"),
        ("PIL", "Pillow"),
        ("gtts", "gTTS"),
        ("werkzeug", "Werkzeug"),
    ]
    
    optional = [
        ("transformers", "Transformers (for AI model)"),
        ("torch", "PyTorch (for AI model)"),
        ("cv2", "OpenCV"),
    ]
    
    # Check required dependencies
    print("Required Dependencies:")
    required_ok = all(check_module(mod, name) for mod, name in required)
    print()
    
    # Check optional dependencies
    print("Optional Dependencies:")
    optional_ok = all(check_module(mod, name) for mod, name in optional)
    print()
    
    # Check Python version
    print("Python Information:")
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠ Warning: Python 3.8 or higher is recommended")
    print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    
    if required_ok:
        print("✓ All required dependencies are installed")
        print("✓ System is ready to run in basic mode")
        print()
        
        if not optional_ok:
            print("⚠ Some optional dependencies are missing")
            print("  The system will run with fallback image descriptions")
            print("  To enable AI-powered descriptions, install:")
            print("    pip install transformers torch")
        else:
            print("✓ All optional dependencies are installed")
            print("✓ System is ready to run with full AI capabilities")
        
        print()
        print("Next steps:")
        print("  1. Run demo: python demo.py")
        print("  2. Start web app: python run.py")
        print("  3. Run tests: python -m unittest discover tests")
    else:
        print("✗ Some required dependencies are missing")
        print("  Please install them with:")
        print("    pip install -r requirements.txt")
        return 1
    
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
