# Quick Start Guide - Intelpod Django Website

## Fast Setup (5 minutes)

### Option 1: Automated Setup (Recommended)

**On macOS/Linux:**
```bash
cd intelpod_website
./setup.sh
```

**On Windows:**
```bash
cd intelpod_website
setup.bat
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# 3. Install packages
pip install -r requirements.txt

# 4. Setup database
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

## First Steps After Setup

### 1. Create Superuser
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### 2. Start the Development Server
```bash
python manage.py runserver
```

### 3. Access the Website
- **Main Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

## Adding Your First Product

1. Go to http://127.0.0.1:8000/admin
2. Login with your superuser credentials
3. Click on "Products" → "Add Product"
4. Fill in the details:
   - **Name**: SvedaPod Classic
   - **Slug**: svedapod-classic (auto-generated)
   - **Description**: Full product description
   - **Short Description**: Brief 1-2 sentence description
   - **Price**: 45000
   - **Original Price**: 50000 (optional, for showing discount)
   - **Stock**: 10
   - **Available**: ✓ (checked)
5. Upload a product image
6. Add specifications (height, length, width, material)
7. Click "Save"

## Adding Sample Data

### Create Benefits:
1. Admin → Benefits → Add Benefit
   - Title: "Detoxification"
   - Description: "Removes toxins from body through sweating"
   - Order: 1

### Create Testimonials:
1. Admin → Testimonials → Add Testimonial
   - Name: "John Doe"
   - Role: "Wellness Coach"
   - Content: "Amazing product! Changed my wellness routine."
   - Rating: 5

## Common Commands

```bash
# Start server
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (production)
python manage.py collectstatic

# Open Django shell
python manage.py shell
```

## Project URLs

- **Home Page**: /
- **Products**: /products/
- **Product Detail**: /product/<slug>/
- **Cart**: /cart/
- **Checkout**: /checkout/
- **Contact**: /contact/
- **About**: /about/
- **Admin**: /admin/

## Customization Quick Tips

### Change Brand Colors:
Edit `static/css/style.css` and modify:
```css
:root {
    --primary-color: #004b27;  /* Your green color */
    --secondary-color: #28a745;
}
```

### Update Contact Info:
Edit `templates/base.html` footer section

### Modify Homepage:
Edit `templates/products/home.html`

## Troubleshooting

**Problem**: Module not found error
**Solution**: Make sure virtual environment is activated and dependencies installed

**Problem**: Static files not loading
**Solution**: Run `python manage.py collectstatic`

**Problem**: Images not displaying
**Solution**: Check that `MEDIA_URL` is configured and media files are uploaded

**Problem**: Can't login to admin
**Solution**: Create superuser with `python manage.py createsuperuser`

## Next Steps

1. ✅ Add your products in admin panel
2. ✅ Upload product images
3. ✅ Add testimonials
4. ✅ Customize colors and branding
5. ✅ Test the shopping cart and checkout flow
6. ✅ Configure email settings (optional)
7. ✅ Deploy to production server

## Production Deployment Checklist

Before deploying to production:

- [ ] Set `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to a new random value
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Configure production database (PostgreSQL recommended)
- [ ] Set up email backend
- [ ] Enable HTTPS
- [ ] Run `collectstatic`
- [ ] Set up backup system
- [ ] Configure payment gateway (if needed)

## Support

Need help? Check the full README.md for detailed documentation.

Happy coding! 🚀
