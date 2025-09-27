#!/usr/bin/env python3
"""
Multi-Platform Video Downloader
Ultra-functional microsystem for downloading videos from TikTok, YouTube, Instagram
with best quality, removing metadata, and saving to output folder.
"""

import os
import sys
import re
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Optional, Dict, Any
import yt_dlp
import ffmpeg


class MultiPlatformDownloader:
    def __init__(self, output_dir: str = "output"):
        """Initialize the multi-platform video downloader."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.temp_dir = Path(tempfile.mkdtemp())
        
    def __del__(self):
        """Clean up temporary directory."""
        if hasattr(self, 'temp_dir') and self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def validate_url(self, url: str) -> bool:
        """Validate if the URL is supported (TikTok, YouTube, Instagram)."""
        supported_patterns = [
            # TikTok patterns
            r'https?://(?:www\.)?tiktok\.com/@[\w.-]+/video/\d+',
            r'https?://(?:vm|vt)\.tiktok\.com/[\w.-]+',
            r'https?://(?:www\.)?tiktok\.com/t/[\w.-]+',
            r'https?://(?:m\.)?tiktok\.com/v/\d+',

            # YouTube patterns
            r'https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+',
            r'https?://(?:www\.)?youtube\.com/shorts/[\w-]+',
            r'https?://youtu\.be/[\w-]+',
            r'https?://(?:m\.)?youtube\.com/watch\?v=[\w-]+',

            # Instagram patterns
            r'https?://(?:www\.)?instagram\.com/p/[\w-]+',
            r'https?://(?:www\.)?instagram\.com/reel/[\w-]+',
            r'https?://(?:www\.)?instagram\.com/tv/[\w-]+',
            r'https?://(?:www\.)?instagram\.com/stories/[\w.-]+/\d+',
        ]

        return any(re.match(pattern, url) for pattern in supported_patterns)

    def detect_platform(self, url: str) -> str:
        """Detect which platform the URL belongs to."""
        if 'tiktok.com' in url or 'vm.tiktok.com' in url or 'vt.tiktok.com' in url:
            return 'TikTok'
        elif 'youtube.com' in url or 'youtu.be' in url:
            return 'YouTube'
        elif 'instagram.com' in url:
            return 'Instagram'
        else:
            return 'Unknown'
    
    def get_video_info(self, url: str) -> Optional[Dict[str, Any]]:
        """Get video information without downloading."""
        # Handle all platforms with yt-dlp
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None
    
    def download_video(self, url: str) -> Optional[str]:
        """Download video from supported platforms with best quality."""
        if not self.validate_url(url):
            platform = self.detect_platform(url)
            print(f"Error: Invalid or unsupported URL for {platform}")
            print("Supported platforms: TikTok, YouTube, Instagram")
            return None

        platform = self.detect_platform(url)
        print(f"📱 Platform detected: {platform}")

        # Get video info first
        info = self.get_video_info(url)
        if not info:
            return None

        # Generate safe filename based on platform
        title = info.get('title', f'{platform.lower()}_video')
        uploader = info.get('uploader', 'unknown')
        video_id = info.get('id', 'unknown')

        # Clean filename
        safe_title = re.sub(r'[^\w\s-]', '', title)[:50]
        safe_uploader = re.sub(r'[^\w\s-]', '', uploader)[:20]
        filename = f"{safe_uploader}_{safe_title}_{video_id}"

        temp_path = self.temp_dir / f"{filename}.%(ext)s"

        # Platform-specific yt-dlp options
        ydl_opts = self._get_platform_options(platform, str(temp_path))

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"📥 Downloading: {info.get('title', 'Unknown title')}")
                print(f"👤 Uploader: {info.get('uploader', 'Unknown')}")
                duration = info.get('duration')
                if duration:
                    print(f"⏱️ Duration: {duration} seconds")

                ydl.download([url])

                # Find the downloaded file
                downloaded_files = list(self.temp_dir.glob(f"{filename}.*"))
                if downloaded_files:
                    return str(downloaded_files[0])
                else:
                    print("Error: Downloaded file not found")
                    return None

        except Exception as e:
            print(f"Error downloading video: {e}")
            return None

    def download_shopee_video(self, url: str) -> Optional[str]:
        """Download video from Shopee product page."""
        try:
            print(f"🛍️ Processing Shopee URL: {url}")

            # Get video info from Shopee
            info = self.shopee_extractor.get_video_info(url)
            if not info:
                print("❌ No videos found on this Shopee product page")
                return None

            video_urls = info.get('video_urls', [])
            if not video_urls:
                print("❌ No video URLs found")
                return None

            print(f"📥 Found {len(video_urls)} video(s)")
            print(f"📝 Product: {info.get('title', 'Unknown')}")
            print(f"🏪 Shop: {info.get('uploader', 'Unknown')}")

            # Download the first video (or all videos if multiple)
            downloaded_files = []
            for i, video_url in enumerate(video_urls, 1):
                print(f"\n📥 Downloading video {i}/{len(video_urls)}...")

                # Create filename
                safe_title = re.sub(r'[^\w\s-]', '', info.get('title', 'shopee_video'))[:50]
                safe_shop = re.sub(r'[^\w\s-]', '', info.get('uploader', 'unknown'))[:20]
                video_id = info.get('id', 'unknown')
                filename = f"shopee_{safe_shop}_{safe_title}_{video_id}_{i}.mp4"

                output_path = self.output_dir / filename

                # Download video
                if self.shopee_extractor.download_video(video_url, str(output_path)):
                    # Remove metadata if ffmpeg is available
                    clean_path = self.output_dir / f"clean_{filename}"
                    if self.remove_metadata(output_path, clean_path):
                        output_path.unlink()  # Remove original
                        downloaded_files.append(str(clean_path))
                        print(f"✅ Video saved: {clean_path}")
                    else:
                        downloaded_files.append(str(output_path))
                        print(f"✅ Video saved (metadata not removed): {output_path}")
                else:
                    print(f"❌ Failed to download video {i}")

            if downloaded_files:
                return downloaded_files[0]  # Return first downloaded file
            else:
                return None

        except Exception as e:
            print(f"❌ Error downloading Shopee video: {e}")
            return None

    def _get_platform_options(self, platform: str, temp_path: str) -> Dict[str, Any]:
        """Get platform-specific yt-dlp options."""
        base_opts = {
            'outtmpl': temp_path,
            'writeinfojson': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
            'ignoreerrors': False,
            'no_warnings': False,
        }

        if platform == 'TikTok':
            base_opts['format'] = 'best[height<=1080]/best'
        elif platform == 'YouTube':
            # For YouTube, prefer mp4 format and reasonable quality
            base_opts['format'] = 'best[ext=mp4][height<=1080]/best[height<=1080]/best'
        elif platform == 'Instagram':
            # Instagram specific options
            base_opts['format'] = 'best[height<=1080]/best'
            # Instagram may require cookies for some content
            base_opts['cookiefile'] = None  # User can add cookie file if needed

        return base_opts
    
    def remove_metadata(self, input_path: str, output_path: str) -> bool:
        """Remove all metadata from video using ffmpeg."""
        try:
            print("Removing metadata...")

            # Use ffmpeg to remove metadata
            (
                ffmpeg
                .input(input_path)
                .output(
                    output_path,
                    map_metadata=-1,  # Remove all metadata
                    c='copy',         # Copy streams without re-encoding
                    avoid_negative_ts='make_zero'
                )
                .overwrite_output()
                .run(quiet=True, capture_stdout=True)
            )

            return True

        except ffmpeg.Error as e:
            print(f"Error removing metadata: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    def process_video(self, url: str) -> Optional[str]:
        """Complete process: download, remove metadata, and save."""
        print(f"Processing TikTok URL: {url}")
        
        # Download video
        temp_video_path = self.download_video(url)
        if not temp_video_path:
            return None
        
        # Generate output filename
        temp_path = Path(temp_video_path)
        output_filename = f"clean_{temp_path.stem}.mp4"
        output_path = self.output_dir / output_filename
        
        # Remove metadata
        if self.remove_metadata(temp_video_path, str(output_path)):
            print(f"✅ Video saved successfully: {output_path}")
            
            # Show file info
            file_size = output_path.stat().st_size / (1024 * 1024)  # MB
            print(f"📁 File size: {file_size:.2f} MB")
            print(f"📂 Location: {output_path.absolute()}")
            
            return str(output_path)
        else:
            print("❌ Failed to remove metadata")
            return None


def main():
    """Main function for interactive usage."""
    print("🎬 Multi-Platform Video Downloader")
    print("=" * 50)
    print("✅ Supported: TikTok, YouTube, Instagram, Shopee")
    print("📁 Videos will be saved to: output/")
    print("🔄 Press Ctrl+C to exit")
    print("=" * 50)

    # Check if ffmpeg is available
    ffmpeg_available = True
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✅ FFmpeg detected - metadata will be removed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️ FFmpeg not found - videos will be downloaded without metadata removal")
        print("💡 Run 'install_ffmpeg.bat' to install FFmpeg")
        ffmpeg_available = False

    print("=" * 50)

    downloader = MultiPlatformDownloader()

    while True:
        try:
            print("\n📥 Enter video URL (or 'quit' to exit):")
            url = input("URL: ").strip()

            if url.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break

            if not url:
                print("❌ Please enter a valid URL")
                continue

            # Process the URL
            result = downloader.download_video(url)
            if result:
                print(f"✅ Success! Video saved to: {result}")
            else:
                print("❌ Failed to process video")
                print("💡 Try again or check if the video is public")

                # Show help for invalid URLs
                if not downloader.validate_url(url):
                        platform = downloader.detect_platform(url)
                        print(f"❌ Invalid or unsupported URL for {platform}.")
                        print("💡 Supported platforms and formats:")
                        print("   📱 TikTok:")
                        print("      - https://www.tiktok.com/@user/video/123")
                        print("      - https://vm.tiktok.com/ZMexample")
                        print("   📺 YouTube:")
                        print("      - https://www.youtube.com/watch?v=123")
                        print("      - https://youtu.be/123")
                        print("      - https://www.youtube.com/shorts/123")
                        print("   📷 Instagram:")
                        print("      - https://www.instagram.com/p/123")
                        print("      - https://www.instagram.com/reel/123")
                        print("   🛍️ Shopee:")
                        print("      - https://shopee.com.br/produto-i.123.456")
                        print("      - https://shopee.com.my/product-i.123.456")

            print(f"\n🔄 Processing: {url}")
            result = downloader.process_video(url)

            if result:
                print(f"\n🎉 Success! Video saved: {result}")
                if ffmpeg_available:
                    print("✅ Metadata removed successfully")
                else:
                    print("⚠️ Metadata not removed (FFmpeg not available)")
            else:
                print("\n❌ Failed to process video")
                print("💡 Try again or check if the video is public")

            print("\n" + "=" * 50)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("💡 Please try again")


def main_cli():
    """Command line interface for single URL processing."""
    if len(sys.argv) != 2:
        print("Usage: python tiktok_downloader.py <tiktok_url>")
        print("Example: python tiktok_downloader.py https://www.tiktok.com/@user/video/1234567890")
        print("\nOr run without arguments for interactive mode")
        sys.exit(1)

    url = sys.argv[1]

    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: ffmpeg is not installed or not in PATH")
        print("Please install ffmpeg: https://ffmpeg.org/download.html")
        sys.exit(1)

    downloader = MultiPlatformDownloader()
    result = downloader.process_video(url)

    if result:
        print(f"\n🎉 Success! Video downloaded and cleaned: {result}")
    else:
        print("\n❌ Failed to process video")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_cli()  # Command line mode with URL argument
    else:
        main()      # Interactive mode
