@echo off
echo ========================================
echo    Entity Extractor - Web Scraping Tool
echo ========================================
echo.
echo Starting the application...
echo.
echo Please wait while we install dependencies...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Install requirements if needed
echo Installing/updating dependencies...
pip install -r requirements.txt

echo.
echo Dependencies installed successfully!
echo.
echo Starting Streamlit app...
echo.
echo The app will open in your default browser
echo If it doesn't open automatically, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start the Streamlit app
streamlit run app.py

pause
