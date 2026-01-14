# 🚀 Render.com Deployment Guide for Intelpod Website

Complete guide to deploy your Intelpod Django website to Render.com with all images, products, and blog data.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Files Prepared for Deployment](#files-prepared)
3. [Render.com Setup](#render-setup)
4. [Database Configuration](#database-configuration)
5. [Static & Media Files](#static-media-files)
6. [Loading Initial Data](#loading-initial-data)
7. [Environment Variables](#environment-variables)
8. [Post-Deployment Steps](#post-deployment)
9. [Troubleshooting](#troubleshooting)

---

## 📦 Prerequisites

### What You Need:
- ✅ GitHub account (to push your code)
- ✅ Render.com account (free tier available)
- ✅ All data exported to fixtures
- ✅ All images organized in media/static folders

### Current Django Version:
- **Django:** 6.0.1
- **Python:** 3.14.0

---

## 📂 Files Prepared for Deployment

### **1. Data Fixtures** (in `fixtures/` directory)

```
fixtures/
├── products_data.json      # All products, images, features
├── blog_data.json          # All 5 blog posts
└── content_data.json       # Benefits, testimonials, FAQs, team members
```

**Contains:**
- ✅ 4 Products (SvedaPod Classic, Premium, Deluxe, Commercial)
- ✅ 5 Blog Posts (Sleep, Detox, Future Wellness, Skin, Buying Guide)
- ✅ 6 Health Benefits
- ✅ 3+ Testimonials
- ✅ FAQs
- ✅ Team Members (if added)

### **2. Media Files**

#### **Product Images** (`media/products/`):
```
media/products/
├── svedapod-classic.png    (939 KB)
├── svedapod-premium.png    (939 KB)
├── svedapod-deluxe.png     (783 KB)
├── svedapod-commercial.png (264 KB)
└── hero-image.png          (264 KB)
```

#### **Blog Images** (`media/blog/`):
```
media/blog/
├── blog-1-sleep-quality.png       (384 KB)
├── blog-2-detoxify.png            (585 KB)
├── blog-3-future-wellness.png     (1.0 MB)
├── blog-4-better-skin.png         (372 KB)
└── blog-5-choosing-guide.png      (782 KB)
```

#### **Static Images** (`static/images/`):
```
static/images/
├── logo.png                  (13 KB)
├── hero-product.png          (264 KB)
├── gem-certificate.png       (321 KB)
├── startup-india.png         (32 KB)
├── make-in-india.png         (40 KB)
└── about-hero.jpg            (264 KB)
```

**Total Media Size:** ~6.5 MB

### **3. Deployment Scripts**

- ✅ `load_initial_data.py` - Automated data loader
- ✅ `requirements.txt` - Updated with Django 6.0.1
- ✅ `build.sh` - Render build script (to be created)

---

## 🔧 Render.com Setup

### Step 1: Prepare Your Code for Git

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Intelpod website ready for deployment"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/intelpod-website.git
git branch -M main
git push -u origin main
```

### Step 2: Create Build Script

Create `build.sh` in your project root:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Load initial data (only on first deploy)
if [ "$LOAD_INITIAL_DATA" = "true" ]; then
    echo "Loading initial data..."
    python load_initial_data.py
fi
```

Make it executable:
```bash
chmod +x build.sh
```

### Step 3: Update settings.py for Production

Add to `intelpod_website/settings.py`:

```python
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Database
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    # Local SQLite database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Step 4: Update requirements.txt

Add these packages:

```bash
pip install dj-database-url psycopg2-binary whitenoise gunicorn
pip freeze > requirements.txt
```

Your `requirements.txt` should now include:
```
Django==6.0.1
Pillow==11.1.0
dj-database-url==2.2.0
psycopg2-binary==2.9.10
whitenoise==6.8.2
gunicorn==23.0.0
```

---

## 🎯 Render.com Web Service Setup

### 1. Create New Web Service

1. Go to https://render.com/
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select `intelpod-website` repository

### 2. Configure Service

**Basic Settings:**
- **Name:** `intelpod-website`
- **Region:** Choose closest to your users
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn intelpod_website.wsgi:application`

**Instance Type:**
- Start with **Free tier** (can upgrade later)

### 3. Environment Variables

Click "Advanced" and add these environment variables:

| Key | Value | Description |
|-----|-------|-------------|
| `SECRET_KEY` | `your-secret-key-here` | Django secret key (generate new one!) |
| `DEBUG` | `False` | Turn off debug mode |
| `ALLOWED_HOSTS` | `intelpod-website.onrender.com,www.intelpod-website.onrender.com` | Your Render domain |
| `DATABASE_URL` | *Auto-set by Render PostgreSQL* | Leave blank initially |
| `PYTHON_VERSION` | `3.14.0` | Specify Python version |
| `LOAD_INITIAL_DATA` | `true` | Load data on first deploy |

**Generate a new SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 4. Create PostgreSQL Database

1. Click "New +" → "PostgreSQL"
2. **Name:** `intelpod-db`
3. **Database:** `intelpod`
4. **User:** `intelpod_user`
5. Select **Free tier**
6. Click "Create Database"

### 5. Link Database to Web Service

1. Go to your web service settings
2. Under "Environment" → "Add Environment Variable"
3. **Key:** `DATABASE_URL`
4. **Value:** Select your PostgreSQL database from dropdown
5. Render will automatically fill in the connection string

---

## 📤 Static & Media Files Configuration

### Option 1: Whitenoise (Included)

Already configured! Whitenoise will serve static files directly from your app.

### Option 2: Render Disk (For Media Files)

Render's free tier doesn't include persistent disks. For production, use:

**Recommended: AWS S3 or Cloudinary**

#### Using Cloudinary (Free Tier):

1. Install packages:
```bash
pip install cloudinary django-cloudinary-storage
```

2. Add to `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
]

# Cloudinary configuration
import cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

3. Add Cloudinary credentials to Render environment variables

---

## 🗄️ Loading Initial Data

### Method 1: Automatic (First Deploy)

If `LOAD_INITIAL_DATA=true` in environment variables, data loads automatically during build.

### Method 2: Manual (After Deploy)

1. Open Render Shell:
   - Go to your service → "Shell" tab

2. Run data loader:
```bash
python load_initial_data.py
```

### Method 3: Django Admin

After first deploy:

1. Create superuser:
```bash
python manage.py createsuperuser
```

2. Login to `/admin/`
3. Manually add products and content

### What Gets Loaded:

✅ **4 Products:**
- SvedaPod Classic (₹45,000)
- SvedaPod Premium (₹75,000)
- SvedaPod Deluxe (₹60,000)
- SvedaPod Commercial (₹1,50,000)

✅ **5 Blog Posts:**
1. How a Steam Bath Cabinet Can Improve Your Sleep Quality
2. The Science Behind Steam Baths: How They Help Detoxify Your Body
3. The Future of Home Wellness
4. Why Steam Bath Cabinets Are the Secret to Better Skin
5. The Ultimate Guide to Choosing the Best Steam Bath Cabinet

✅ **Content:**
- 6 Health Benefits
- 3+ Customer Testimonials
- FAQs
- Team Members

---

## 🔐 Environment Variables Reference

### Required Variables:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.onrender.com

# Database (auto-set by Render PostgreSQL)
DATABASE_URL=postgresql://user:pass@host:5432/db

# Python Version
PYTHON_VERSION=3.14.0

# Deployment
LOAD_INITIAL_DATA=true  # Set to false after first deploy
```

### Optional Variables (if using Cloudinary):

```bash
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

---

## ✅ Post-Deployment Steps

### 1. Verify Deployment

Visit your Render URL: `https://intelpod-website.onrender.com`

### 2. Check Admin Panel

Go to: `https://intelpod-website.onrender.com/admin/`

**Default credentials (if loaded via script):**
- Username: `admin`
- Password: `admin123`

**⚠️ CHANGE THIS IMMEDIATELY!**

### 3. Test All Pages

- ✅ Homepage: `/`
- ✅ Products: `/products/`
- ✅ Product Detail: `/products/svedapod-classic/`
- ✅ Blog: `/blog/`
- ✅ Blog Detail: `/blog/how-a-steam-bath-cabinet-can-improve-your-sleep-quality/`
- ✅ About: `/about/`
- ✅ Contact: `/contact/`
- ✅ Cart: `/cart/`

### 4. Upload Missing Images (if any)

If images aren't showing:

1. Go to `/admin/`
2. Navigate to Products → Product
3. Edit each product
4. Re-upload images through admin interface

### 5. Configure Custom Domain (Optional)

**If you have your own domain:**

1. Go to Render service → "Settings"
2. Under "Custom Domain" → "Add Custom Domain"
3. Enter your domain: `www.intelpod.in`
4. Add DNS records as shown by Render:
   ```
   Type: CNAME
   Name: www
   Value: intelpod-website.onrender.com
   ```

---

## 🐛 Troubleshooting

### Issue 1: Static Files Not Loading

**Solution:**
```bash
# In Render Shell
python manage.py collectstatic --no-input
```

Check `settings.py`:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Issue 2: Database Connection Error

**Check:**
1. PostgreSQL database is created
2. `DATABASE_URL` environment variable is set
3. Connection string is correct

**Test connection:**
```bash
python manage.py dbshell
```

### Issue 3: Images Not Showing

**Causes:**
- Media files not uploaded
- `MEDIA_URL` and `MEDIA_ROOT` not configured
- Missing images in `media/` folder

**Solutions:**
1. Use Cloudinary for media storage (recommended)
2. Upload images via admin panel
3. Ensure images are in correct folders

### Issue 4: 502 Bad Gateway

**Causes:**
- Build failed
- Application crashed on startup
- Missing dependencies

**Check:**
1. Render logs for errors
2. `requirements.txt` is complete
3. `build.sh` executed successfully

**Fix:**
```bash
# Check logs in Render dashboard
# Look for Python errors
```

### Issue 5: Data Not Loaded

**Solution:**
```bash
# In Render Shell
python load_initial_data.py

# Or load individually
python manage.py loaddata fixtures/products_data.json
python manage.py loaddata fixtures/blog_data.json
python manage.py loaddata fixtures/content_data.json
```

### Issue 6: Admin CSS/JS Not Loading

**Solution:**
```bash
python manage.py collectstatic --no-input
```

Ensure in `settings.py`:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## 📊 Deployment Checklist

Before going live, verify:

- [ ] All environment variables set correctly
- [ ] PostgreSQL database created and linked
- [ ] Build script runs without errors
- [ ] Static files collected successfully
- [ ] Migrations applied
- [ ] Initial data loaded (products, blog posts)
- [ ] All images visible
- [ ] Admin panel accessible
- [ ] Default admin password changed
- [ ] All pages load correctly
- [ ] Forms work (contact, cart)
- [ ] SSL certificate active (https://)
- [ ] Custom domain configured (if applicable)
- [ ] Google Analytics added (optional)
- [ ] SEO meta tags verified
- [ ] 404/500 error pages work

---

## 🚀 Deployment Commands Summary

### Push to GitHub:
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Render Will Automatically:
1. Clone your repository
2. Run `./build.sh`
3. Install dependencies
4. Collect static files
5. Run migrations
6. Load initial data (if LOAD_INITIAL_DATA=true)
7. Start with `gunicorn`

### Manual Commands (if needed):
```bash
# In Render Shell

# Create superuser
python manage.py createsuperuser

# Load data
python load_initial_data.py

# Collect static
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Check database
python manage.py dbshell
```

---

## 💰 Cost Estimation

### Free Tier (Good for testing):
- ✅ Web Service: Free (sleeps after 15 min inactivity)
- ✅ PostgreSQL: 90-day free trial, then $7/month
- ⚠️ **Total: $0 for 90 days, then $7/month**

### Paid Tier (Recommended for production):
- Web Service: $7/month (always on, faster)
- PostgreSQL: $7/month
- Disk Storage: $1/GB/month (if needed)
- **Total: ~$15-20/month**

### Cloudinary (for images):
- Free tier: 25GB storage, 25GB bandwidth/month
- **Total: $0 for most small sites**

---

## 📞 Support & Resources

### Render Documentation:
- https://render.com/docs/deploy-django
- https://render.com/docs/databases

### Django Documentation:
- https://docs.djangoproject.com/en/6.0/howto/deployment/

### Your Project Files:
- `fixtures/` - All data exports
- `media/` - All images
- `load_initial_data.py` - Data loader script
- `requirements.txt` - Python dependencies
- `build.sh` - Render build script

---

## 🎉 Success!

Once deployed, your Intelpod website will have:

✅ **4 Products** with images and features
✅ **5 Blog Posts** with featured images
✅ **Health Benefits** section
✅ **Customer Testimonials**
✅ **FAQs**
✅ **Contact Form**
✅ **Shopping Cart**
✅ **Admin Panel**
✅ **Responsive Design**
✅ **SEO Optimized**
✅ **SSL Certificate**

Your website will be live at:
```
https://intelpod-website.onrender.com
```

---

## 📝 Next Steps After Deployment

1. **Change admin password immediately**
2. **Test all functionality**
3. **Add Google Analytics**
4. **Submit sitemap to Google Search Console**
5. **Set up email notifications**
6. **Configure payment gateway (Razorpay/Stripe)**
7. **Add WhatsApp chat widget**
8. **Set up automated backups**

---

**Your Intelpod website is ready to deploy! 🚀**

*Created: January 14, 2026*
*Django Version: 6.0.1*
*Python Version: 3.14.0*
