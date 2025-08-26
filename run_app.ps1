# Entity Extractor - Web Scraping Tool Launcher
# PowerShell Script

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Entity Extractor - Web Scraping Tool" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ and try again" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if pip is available
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✅ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: pip is not available" -ForegroundColor Red
    Write-Host "Please ensure pip is installed with Python" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "📦 Installing/updating dependencies..." -ForegroundColor Yellow

# Install requirements
try {
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Failed to install dependencies" -ForegroundColor Red
    Write-Host "Please check your internet connection and try again" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "🚀 Starting Streamlit app..." -ForegroundColor Green
Write-Host ""
Write-Host "The app will open in your default browser" -ForegroundColor Cyan
Write-Host "If it doesn't open automatically, go to: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

# Start the Streamlit app
try {
    streamlit run app.py
} catch {
    Write-Host "❌ ERROR: Failed to start Streamlit app" -ForegroundColor Red
    Write-Host "Please ensure all dependencies are installed correctly" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
