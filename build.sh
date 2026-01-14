#!/usr/bin/env bash
# Render.com Build Script for Intelpod Website
# exit on error
set -o errexit

echo "=========================================="
echo "Starting Intelpod Website Build Process"
echo "=========================================="

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --no-input

# Copy media files into staticfiles directory for WhiteNoise
echo "🖼️  Copying media files to staticfiles..."
if [ -d "media" ]; then
    cp -r media staticfiles/
    echo "✓ Media files copied to staticfiles/media/"
    echo "   Files: $(find staticfiles/media -type f | wc -l)"
else
    echo "⚠️  Warning: media directory not found"
fi

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# Load initial data (only if LOAD_INITIAL_DATA is true)
if [ "$LOAD_INITIAL_DATA" = "true" ]; then
    echo "📊 Loading initial data..."
    python load_initial_data.py
else
    echo "⏭️  Skipping initial data load (set LOAD_INITIAL_DATA=true to enable)"
fi

echo "=========================================="
echo "Build completed successfully! ✅"
echo "=========================================="
