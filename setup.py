#!/usr/bin/env python3
"""
Setup script for TikTok Downloader
Installs dependencies and checks system requirements.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True


def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✅ ffmpeg is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg is not installed")
        print("Please install ffmpeg:")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("  macOS: brew install ffmpeg")
        print("  Ubuntu/Debian: sudo apt install ffmpeg")
        print("  CentOS/RHEL: sudo yum install ffmpeg")
        return False


def install_requirements():
    """Install Python requirements."""
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    command = f"{sys.executable} -m pip install -r requirements.txt"
    return run_command(command, "Installing Python dependencies")


def create_output_directory():
    """Create output directory."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    print(f"✅ Output directory created: {output_dir.absolute()}")
    return True


def main():
    """Main setup function."""
    print("🚀 Setting up TikTok Downloader...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check ffmpeg
    if not check_ffmpeg():
        print("\n⚠️  Setup will continue, but ffmpeg is required for metadata removal")
        print("The downloader will work but won't remove metadata without ffmpeg")
    
    # Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements")
        sys.exit(1)
    
    # Create output directory
    create_output_directory()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nUsage:")
    print("  python tiktok_downloader.py <tiktok_url>")
    print("\nExample:")
    print("  python tiktok_downloader.py https://www.tiktok.com/@user/video/1234567890")
    print(f"\nVideos will be saved to: {Path('output').absolute()}")


if __name__ == "__main__":
    main()
