#!/usr/bin/env python3
"""
Setup script for Entity Extractor
Automates the installation and setup process
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    
    if sys.version_info < (3, 8):
        print(f"❌ Python 3.8+ required, found {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True

def check_pip():
    """Check if pip is available"""
    print("📦 Checking pip availability...")
    
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, check=True)
        print(f"✅ pip is available: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ pip is not available")
        return False

def install_requirements():
    """Install required packages"""
    print("📚 Installing required packages...")
    
    # Upgrade pip first
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing requirements"):
        return False
    
    return True

def create_virtual_environment():
    """Create a virtual environment (optional)"""
    print("🏗️ Creating virtual environment...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    if not run_command(f"{sys.executable} -m venv venv", "Creating virtual environment"):
        return False
    
    print("✅ Virtual environment created successfully")
    print("💡 To activate it:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/Mac
        print("   source venv/bin/activate")
    
    return True

def test_installation():
    """Test if the installation was successful"""
    print("🧪 Testing installation...")
    
    try:
        # Test importing key modules
        import streamlit
        import pandas
        import requests
        import bs4
        import selenium
        
        print("✅ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def show_next_steps():
    """Show next steps for the user"""
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the demo script to see sample data:")
    print("   python demo.py")
    print()
    print("2. Start the Streamlit web application:")
    print("   streamlit run app.py")
    print()
    print("3. Or use the provided scripts:")
    if os.name == 'nt':  # Windows
        print("   - Double-click run_app.bat")
        print("   - Or run run_app.ps1 in PowerShell")
    else:
        print("   - Run: ./run_app.sh")
    print()
    print("4. Open your browser and go to: http://localhost:8501")
    print()
    print("📚 For more information, see README.md")

def main():
    """Main setup function"""
    print("🚀 Entity Extractor - Setup Script")
    print("=" * 50)
    print("This script will set up the Entity Extractor tool")
    print("and install all required dependencies.")
    print()
    
    # Check prerequisites
    if not check_python_version():
        print("❌ Setup cannot continue. Please install Python 3.8+")
        sys.exit(1)
    
    if not check_pip():
        print("❌ Setup cannot continue. Please install pip")
        sys.exit(1)
    
    # Ask about virtual environment
    create_venv = input("🤔 Create a virtual environment? (y/n, default: y): ").lower()
    if create_venv in ['', 'y', 'yes']:
        if not create_virtual_environment():
            print("⚠️ Virtual environment creation failed, continuing with global installation")
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed during package installation")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("❌ Setup failed during testing")
        sys.exit(1)
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error during setup: {e}")
        sys.exit(1)
