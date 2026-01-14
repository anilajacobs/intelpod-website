@echo off
echo ==========================================
echo   Intelpod Website Setup Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3 is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo √ Python 3 found

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv
echo √ Virtual environment created

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate
echo √ Virtual environment activated

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip
echo √ Pip upgraded

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo √ Dependencies installed

REM Run migrations
echo.
echo Running database migrations...
python manage.py makemigrations
python manage.py migrate
echo √ Database migrations completed

REM Create placeholder directories
echo.
echo Creating media directories...
if not exist "media\products" mkdir media\products
if not exist "media\testimonials" mkdir media\testimonials
echo √ Media directories created

echo.
echo ==========================================
echo   Setup Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Create a superuser: python manage.py createsuperuser
echo 2. Start the server: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000
echo 4. Admin panel: http://127.0.0.1:8000/admin
echo.
echo To activate the virtual environment in the future:
echo   venv\Scripts\activate
echo.
pause
