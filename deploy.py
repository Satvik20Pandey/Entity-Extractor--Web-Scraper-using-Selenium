#!/usr/bin/env python3
"""
Deployment Helper Script for Entity Extractor
Guides users through deploying to Streamlit Cloud
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def check_git_status():
    """Check if the repository is ready for deployment"""
    print("🔍 Checking Git repository status...")
    
    try:
        # Check if git is initialized
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Git repository not found. Please initialize git first.")
            return False
        
        # Check for uncommitted changes
        result = subprocess.run(['git', 'diff', '--name-only'], capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️ You have uncommitted changes. Consider committing them first.")
            print("Changed files:")
            for file in result.stdout.strip().split('\n'):
                if file:
                    print(f"  - {file}")
        
        # Check remote origin
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'origin' not in result.stdout:
            print("❌ No remote origin found. Please add a GitHub remote.")
            return False
        
        print("✅ Git repository is ready!")
        return True
        
    except FileNotFoundError:
        print("❌ Git not found. Please install Git first.")
        return False
    except Exception as e:
        print(f"❌ Error checking git status: {e}")
        return False

def check_deployment_files():
    """Check if all required deployment files exist"""
    print("\n📋 Checking deployment files...")
    
    required_files = [
        'app.py',
        'scraper.py', 
        'requirements.txt',
        '.streamlit/config.toml',
        'packages.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    print("✅ All required deployment files found!")
    return True

def show_deployment_steps():
    """Show step-by-step deployment instructions"""
    print("\n🚀 Deployment Steps to Streamlit Cloud")
    print("=" * 50)
    
    print("""
1. 📤 Push to GitHub:
   git add .
   git commit -m "Ready for Streamlit deployment"
   git push origin main

2. 🌐 Go to Streamlit Cloud:
   Visit: https://share.streamlit.io
   Sign in with GitHub

3. ➕ Create New App:
   - Click "New app"
   - Repository: your-username/Extractor
   - Branch: main
   - Main file path: app.py
   - App URL: Leave blank

4. 🚀 Deploy:
   - Click "Deploy!"
   - Wait 2-5 minutes for build
   - Get your public URL!

5. 🧪 Test Your App:
   - Visit your public URL
   - Test with example URLs
   - Share with others!
""")

def open_streamlit_cloud():
    """Open Streamlit Cloud in browser"""
    try:
        print("\n🌐 Opening Streamlit Cloud in your browser...")
        webbrowser.open('https://share.streamlit.io')
        print("✅ Streamlit Cloud opened!")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print("Please manually visit: https://share.streamlit.io")

def create_github_repo_guide():
    """Show guide for creating GitHub repository"""
    print("\n📚 GitHub Repository Setup Guide")
    print("=" * 40)
    
    print("""
If you don't have a GitHub repository yet:

1. 🆕 Go to GitHub.com and sign in
2. ➕ Click "New repository"
3. 📝 Repository name: Extractor
4. 📄 Description: Entity Extractor - Web Scraping Tool
5. 🔒 Choose Public or Private
6. ✅ Check "Add a README file"
7. 🚀 Click "Create repository"

Then in your local folder:
git remote add origin https://github.com/YOUR_USERNAME/Extractor.git
git branch -M main
git push -u origin main
""")

def main():
    """Main deployment helper function"""
    print("🚀 Entity Extractor - Deployment Helper")
    print("=" * 50)
    print("This script will help you deploy your app to Streamlit Cloud")
    print()
    
    # Check prerequisites
    if not check_git_status():
        print("\n❌ Please fix Git issues before proceeding.")
        create_github_repo_guide()
        return
    
    if not check_deployment_files():
        print("\n❌ Please ensure all deployment files exist before proceeding.")
        return
    
    # Show deployment steps
    show_deployment_steps()
    
    # Ask user what they want to do
    print("\n🎯 What would you like to do?")
    print("1. Push to GitHub")
    print("2. Open Streamlit Cloud")
    print("3. Show GitHub setup guide")
    print("4. Exit")
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n📤 Pushing to GitHub...")
            os.system("git add .")
            os.system('git commit -m "Ready for Streamlit deployment"')
            os.system("git push origin main")
            print("✅ Pushed to GitHub!")
            
        elif choice == "2":
            open_streamlit_cloud()
            
        elif choice == "3":
            create_github_repo_guide()
            
        elif choice == "4":
            print("👋 Goodbye! Good luck with deployment!")
            
        else:
            print("❌ Invalid choice. Please try again.")
            
    except KeyboardInterrupt:
        print("\n\n👋 Deployment helper interrupted. Good luck!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
