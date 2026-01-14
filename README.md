# Intelpod Website - Django E-commerce Platform

A modern, fully-featured e-commerce website for Intelpod's premium steam bath cabinets, built with Python Django.

## Features

- **Product Management**: Full-featured product catalog with images, specifications, and pricing
- **Shopping Cart**: Session-based shopping cart functionality
- **Order Management**: Complete order processing system with order tracking
- **Testimonials**: Customer review and rating system
- **Contact System**: Contact form for customer inquiries
- **Admin Dashboard**: Comprehensive admin interface for managing all aspects
- **Responsive Design**: Mobile-friendly design using Bootstrap 5
- **Brand Colors**: Matches Intelpod brand identity (Deep green #004b27)

## Technology Stack

- **Backend**: Python 3.14, Django 5.0
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5, Font Awesome 6, Custom CSS
- **Image Handling**: Pillow

## Project Structure

```
intelpod_website/
├── intelpod_website/       # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/               # Products app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Form definitions
│   ├── admin.py           # Admin configuration
│   └── cart.py            # Shopping cart logic
├── templates/             # HTML templates
│   ├── base.html
│   └── products/
├── static/                # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                 # User-uploaded files
├── manage.py
└── requirements.txt
```

## Installation & Setup

### 1. Create Virtual Environment

```bash
cd intelpod_website
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Settings

Edit `intelpod_website/settings.py` and update:
- `SECRET_KEY`: Generate a new secret key for production
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Add your domain name
- Database settings (if not using SQLite)

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Collect Static Files (Production)

```bash
python manage.py collectstatic
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the website.

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin`

Use the superuser credentials you created to log in.

### Admin Features:
- Add/Edit/Delete Products
- Manage Product Images and Features
- View and Process Orders
- Manage Testimonials
- View Contact Messages
- Configure Benefits

## Adding Products

1. Log in to the admin panel
2. Go to "Products" → "Add Product"
3. Fill in product details:
   - Name, slug, description
   - Price and stock information
   - Specifications (height, length, width, material)
   - Upload product images
4. Add product features through the inline forms
5. Save the product

## Configuration

### Email Settings (Optional)

To enable email notifications for orders, add to `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### Payment Gateway Integration (Future)

The current version uses COD (Cash on Delivery) and Bank Transfer. To integrate payment gateways like Razorpay or PayPal:

1. Install the payment gateway SDK
2. Add configuration to settings.py
3. Update the checkout view in `products/views.py`

## Deployment

### For Production Deployment:

1. **Update Settings**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for sensitive data
   - Configure production database

2. **Security Checklist**:
   - Change SECRET_KEY
   - Enable HTTPS
   - Configure CSRF and CORS settings
   - Set up proper file permissions

3. **Recommended Hosting**:
   - **PythonAnywhere** (Easy deployment)
   - **Heroku** (With PostgreSQL addon)
   - **AWS EC2** (Full control)
   - **DigitalOcean** (Affordable VPS)

### Database Migration

To use PostgreSQL instead of SQLite:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'intelpod_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Install PostgreSQL adapter:
```bash
pip install psycopg2-binary
```

## Customization

### Changing Colors

Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #004b27;
    --primary-dark: #003319;
    --secondary-color: #28a745;
}
```

### Adding Pages

1. Create view in `products/views.py`
2. Add URL pattern in `products/urls.py`
3. Create template in `templates/products/`

## Troubleshooting

### Images Not Displaying

Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured correctly and the development server is serving media files.

### Static Files Not Loading

Run `python manage.py collectstatic` and ensure `STATIC_ROOT` is configured.

### Database Errors

Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## Support

For issues or questions:
- Email: info@intelpod.in
- Check Django documentation: https://docs.djangoproject.com/

## License

Copyright © 2024 Intelpod. All rights reserved.

## Version

Current Version: 1.0.0
Django Version: 5.0.1
Python Version: 3.14+
