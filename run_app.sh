#!/bin/bash

# Entity Extractor - Web Scraping Tool Launcher
# Unix/Linux Shell Script

echo "========================================"
echo "   Entity Extractor - Web Scraping Tool"
echo "========================================"
echo ""

# Check if Python is installed
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ ERROR: Python is not installed or not in PATH"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
echo "✅ Python found: $PYTHON_VERSION"

# Check if pip is available
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    echo "❌ ERROR: pip is not available"
    echo "Please ensure pip is installed with Python"
    exit 1
fi

PIP_VERSION=$($PIP_CMD --version 2>&1)
echo "✅ pip found: $PIP_VERSION"

echo ""
echo "📦 Installing/updating dependencies..."

# Install requirements
if $PIP_CMD install -r requirements.txt; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ ERROR: Failed to install dependencies"
    echo "Please check your internet connection and try again"
    exit 1
fi

echo ""
echo "🚀 Starting Streamlit app..."
echo ""
echo "The app will open in your default browser"
echo "If it doesn't open automatically, go to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Start the Streamlit app
if command -v streamlit &> /dev/null; then
    streamlit run app.py
else
    echo "❌ ERROR: Streamlit not found. Installing..."
    $PIP_CMD install streamlit
    streamlit run app.py
fi
