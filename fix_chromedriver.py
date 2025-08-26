#!/usr/bin/env python3
"""
ChromeDriver Fix Script for Windows
Helps resolve ChromeDriver architecture issues
"""

import os
import platform
import sys
import shutil
import requests
import zipfile
from pathlib import Path

def check_system():
    """Check system information"""
    print("🔍 System Information")
    print("=" * 40)
    print(f"Operating System: {platform.system()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Machine: {platform.machine()}")
    print(f"Python Version: {sys.version}")
    print()

def clear_chromedriver_cache():
    """Clear existing ChromeDriver cache"""
    print("🧹 Clearing ChromeDriver Cache")
    print("=" * 40)
    
    cache_paths = [
        os.path.expanduser("~/.wdm/drivers/chromedriver"),
        os.path.expanduser("~/.wdm"),
        os.path.expanduser("~/.cache/selenium"),
        os.path.expanduser("~/.cache/webdriver")
    ]
    
    for cache_path in cache_paths:
        if os.path.exists(cache_path):
            try:
                shutil.rmtree(cache_path)
                print(f"✅ Cleared: {cache_path}")
            except Exception as e:
                print(f"⚠️ Could not clear {cache_path}: {e}")
        else:
            print(f"ℹ️ Not found: {cache_path}")
    
    print()

def download_chromedriver_manual():
    """Manually download ChromeDriver for Windows"""
    print("📥 Manual ChromeDriver Download")
    print("=" * 40)
    
    if platform.system() != "Windows":
        print("❌ This script is for Windows only")
        return False
    
    # Get Chrome version
    try:
        import subprocess
        result = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            chrome_version = result.stdout.strip()
            print(f"✅ Chrome version: {chrome_version}")
        else:
            # Try alternative method
            result = subprocess.run(['chrome', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                chrome_version = result.stdout.strip()
                print(f"✅ Chrome version: {chrome_version}")
            else:
                print("⚠️ Could not detect Chrome version, using latest")
                chrome_version = "latest"
    except Exception as e:
        print(f"⚠️ Could not detect Chrome version: {e}")
        chrome_version = "latest"
    
    # Download ChromeDriver
    try:
        # Set environment variables for webdriver-manager
        os.environ['WDM_ARCHITECTURE'] = '64'
        os.environ['WDM_PLATFORM'] = 'win64'
        os.environ['WDM_LOG_LEVEL'] = '0'  # Reduce logging
        
        from webdriver_manager.chrome import ChromeDriverManager
        
        print("🔄 Downloading ChromeDriver...")
        driver_path = ChromeDriverManager().install()
        print(f"✅ ChromeDriver downloaded to: {driver_path}")
        
        # Test the driver
        print("🧪 Testing ChromeDriver...")
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.google.com")
        print("✅ ChromeDriver test successful!")
        driver.quit()
        
        return True
        
    except Exception as e:
        print(f"❌ ChromeDriver download failed: {e}")
        return False

def install_chromedriver_alternative():
    """Alternative ChromeDriver installation method"""
    print("🔄 Alternative Installation Method")
    print("=" * 40)
    
    print("📋 Manual steps to install ChromeDriver:")
    print("1. Go to: https://chromedriver.chromium.org/downloads")
    print("2. Download the version matching your Chrome browser")
    print("3. Extract the zip file")
    print("4. Place chromedriver.exe in a folder in your PATH")
    print("5. Or place it in the same folder as this script")
    print()
    
    # Check if chromedriver.exe exists in current directory
    if os.path.exists("chromedriver.exe"):
        print("✅ Found chromedriver.exe in current directory")
        return True
    else:
        print("❌ chromedriver.exe not found in current directory")
        return False

def main():
    """Main function"""
    print("🔧 ChromeDriver Fix Script for Windows")
    print("=" * 50)
    print("This script helps resolve ChromeDriver architecture issues")
    print()
    
    # Check system
    check_system()
    
    if platform.system() != "Windows":
        print("❌ This script is for Windows only")
        print("For other systems, use: pip install webdriver-manager --upgrade")
        return
    
    # Clear cache
    clear_chromedriver_cache()
    
    # Try automatic download
    print("🚀 Attempting automatic ChromeDriver download...")
    if download_chromedriver_manual():
        print("\n🎉 ChromeDriver setup successful!")
        print("You can now run the Entity Extractor with Selenium enabled.")
    else:
        print("\n⚠️ Automatic download failed. Trying alternative method...")
        if install_chromedriver_alternative():
            print("\n💡 ChromeDriver found. Try running the app again.")
        else:
            print("\n❌ ChromeDriver setup failed.")
            print("\n🔧 Troubleshooting steps:")
            print("1. Update Chrome browser to latest version")
            print("2. Restart your computer")
            print("3. Try running: pip install webdriver-manager --upgrade")
            print("4. Check Windows Defender/firewall settings")
            print("5. Run as administrator if needed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Script interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("Please check the error and try again.")
