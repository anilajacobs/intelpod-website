#!/usr/bin/env python
"""
Initial Data Loader for Intelpod Website
Run this script after deploying to Render.com to load all products, blog posts, and content.

Usage:
    python load_initial_data.py
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelpod_website.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User


def load_initial_data():
    """Load all initial data fixtures"""

    print("=" * 60)
    print("INTELPOD WEBSITE - INITIAL DATA LOADER")
    print("=" * 60)
    print()

    # Step 1: Create superuser if doesn't exist
    print("Step 1: Creating admin user...")
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@intelpod.in',
                password='admin123'  # Change this in production!
            )
            print("✓ Admin user created successfully")
            print("  Username: admin")
            print("  Password: admin123")
            print("  ⚠️  IMPORTANT: Change this password immediately!")
        else:
            print("✓ Admin user already exists")
    except Exception as e:
        print(f"✗ Error creating admin user: {e}")
    print()

    # Step 2: Load products data
    print("Step 2: Loading products data...")
    try:
        call_command('loaddata', 'fixtures/products_data.json')
        print("✓ Products, images, and features loaded successfully")
    except Exception as e:
        print(f"✗ Error loading products: {e}")
    print()

    # Step 3: Load blog posts
    print("Step 3: Loading blog posts...")
    try:
        call_command('loaddata', 'fixtures/blog_data.json')
        print("✓ Blog posts loaded successfully")
    except Exception as e:
        print(f"✗ Error loading blog posts: {e}")
    print()

    # Step 4: Load content (benefits, testimonials, FAQs, team)
    print("Step 4: Loading content data...")
    try:
        call_command('loaddata', 'fixtures/content_data.json')
        print("✓ Benefits, testimonials, FAQs, and team members loaded")
    except Exception as e:
        print(f"✗ Error loading content: {e}")
    print()

    # Step 5: Summary
    print("=" * 60)
    print("DATA LOADING COMPLETE!")
    print("=" * 60)
    print()
    print("✓ Your website now has:")

    from products.models import Product, BlogPost, Benefit, Testimonial, FAQ

    print(f"  - {Product.objects.count()} Products")
    print(f"  - {BlogPost.objects.count()} Blog Posts")
    print(f"  - {Benefit.objects.count()} Health Benefits")
    print(f"  - {Testimonial.objects.count()} Testimonials")
    print(f"  - {FAQ.objects.count()} FAQs")
    print()
    print("Next steps:")
    print("1. Login to admin: /admin/")
    print("2. Change admin password immediately")
    print("3. Upload any missing images through admin")
    print("4. Test all pages to ensure everything works")
    print()
    print("=" * 60)


if __name__ == '__main__':
    load_initial_data()
