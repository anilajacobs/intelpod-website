#!/bin/bash

echo "=========================================="
echo "  Intelpod Website Setup Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip
echo "✓ Pip upgraded"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Run migrations
echo ""
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate
echo "✓ Database migrations completed"

# Create placeholder directories
echo ""
echo "Creating media directories..."
mkdir -p media/products
mkdir -p media/testimonials
echo "✓ Media directories created"

# Collect static files
echo ""
echo "Note: Run 'python manage.py collectstatic' for production deployment"

echo ""
echo "=========================================="
echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Create a superuser: python manage.py createsuperuser"
echo "2. Start the server: python manage.py runserver"
echo "3. Visit: http://127.0.0.1:8000"
echo "4. Admin panel: http://127.0.0.1:8000/admin"
echo ""
echo "To activate the virtual environment in the future:"
echo "  source venv/bin/activate"
echo ""
