"""
Load Products with Images
Run: python manage.py shell < load_products_with_images.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelpod_website.settings')
django.setup()

from products.models import Product, Benefit, Testimonial, Feature, ProductImage
from django.utils.text import slugify

print("="*60)
print("Loading Products with Images for Intelpod")
print("="*60)

# Create Benefits
benefits_data = [
    {
        'title': 'Detoxification',
        'description': 'Removes toxins from your body through natural sweating process, promoting overall health and wellness',
        'icon': 'fas fa-droplet',
        'order': 1
    },
    {
        'title': 'Stress Relief',
        'description': 'Reduces stress and anxiety, promotes relaxation and mental clarity for better wellbeing',
        'icon': 'fas fa-heart',
        'order': 2
    },
    {
        'title': 'Respiratory Health',
        'description': 'Improves respiratory function, clears airways, and helps with breathing problems',
        'icon': 'fas fa-lungs',
        'order': 3
    },
    {
        'title': 'Skin Rejuvenation',
        'description': 'Enhances skin health, promotes natural glow, and helps with various skin conditions',
        'icon': 'fas fa-spa',
        'order': 4
    },
    {
        'title': 'Weight Management',
        'description': 'Aids in weight loss, improves metabolism, and helps burn calories naturally',
        'icon': 'fas fa-weight-scale',
        'order': 5
    },
    {
        'title': 'Pain Relief',
        'description': 'Alleviates muscle and joint pain, reduces inflammation, and promotes faster recovery',
        'icon': 'fas fa-hand-holding-medical',
        'order': 6
    }
]

print("\n1. Creating Health Benefits...")
for benefit_data in benefits_data:
    benefit, created = Benefit.objects.get_or_create(
        title=benefit_data['title'],
        defaults=benefit_data
    )
    if created:
        print(f"   ✓ Created: {benefit.title}")
    else:
        print(f"   - Already exists: {benefit.title}")

# Create Main Product - SvedaPod Classic
print("\n2. Creating SvedaPod Classic Product...")
product_data = {
    'name': 'SvedaPod Classic',
    'slug': 'svedapod-classic',
    'description': '''The SvedaPod Classic is our flagship steam bath cabinet, meticulously designed to bring the authentic Ayurvedic steam therapy experience to your home or wellness center.

**Premium Construction**
Crafted with high-quality FRP (Fiber Reinforced Plastic) material, this cabinet offers exceptional durability, superior hygiene, and effortless maintenance. The non-porous surface prevents bacterial growth and is easy to clean, ensuring a safe and sanitary environment for every session.

**Ergonomic Design**
Our ergonomic design ensures maximum comfort during your steam sessions. The spacious interior accommodates users of various heights, while the adjustable seating system provides optimal positioning for the best therapeutic results. The thoughtfully designed door closure ensures steam retention while allowing easy entry and exit.

**Advanced Steam Technology**
The integrated steam generation system delivers consistent, therapeutic steam at the perfect temperature. The system is designed for safety and efficiency, with automatic controls that maintain optimal steam levels throughout your session.

**Perfect For:**
- Home wellness enthusiasts seeking daily detoxification
- Ayurvedic centers and traditional wellness practices
- Modern spas and wellness clinics
- Yoga studios and fitness centers
- Rehabilitation and physiotherapy centers
- Hotels and resorts with spa facilities

**Health Benefits:**
Regular use of the SvedaPod Classic can help with detoxification, stress relief, improved respiratory health, skin rejuvenation, weight management, and natural pain relief. The therapeutic steam opens pores, increases circulation, and promotes overall wellness.

**Quality Assurance:**
Each SvedaPod Classic unit undergoes rigorous quality testing before leaving our facility. We stand behind our product with comprehensive support and guidance for optimal use.

**Made in India:**
Proudly manufactured in India under the Make in India initiative, supporting local craftsmanship and contributing to the nation's growth. We are recognized by Startup India and approved for Government e-Marketplace (GeM) procurement.''',
    'short_description': 'Premium FRP steam bath cabinet with ergonomic design, integrated steam technology, and authentic Ayurvedic wellness experience',
    'price': 45000.00,
    'original_price': 50000.00,
    'stock': 15,
    'available': True,
    'height': '140 cm',
    'length': '135 cm',
    'width': '75 cm',
    'material': 'FRP (Fiber Reinforced Plastic)',
    'meta_title': 'SvedaPod Classic - Premium Steam Bath Cabinet | Made in India',
    'meta_description': 'Buy SvedaPod Classic steam bath cabinet. Premium FRP construction, ergonomic design, integrated steam system. Perfect for home, spa, and Ayurvedic centers.',
    'image': 'products/svedapod-classic.png'
}

product, created = Product.objects.get_or_create(
    slug=product_data['slug'],
    defaults=product_data
)

if created:
    print(f"   ✓ Created product: {product.name}")

    # Add product features
    print("\n3. Adding Product Features...")
    features_data = [
        {
            'title': 'Premium FRP Construction',
            'description': 'Made with high-quality Fiber Reinforced Plastic ensuring durability, hygiene, and long-lasting performance',
            'icon': 'fas fa-shield-alt',
            'order': 1
        },
        {
            'title': 'Ergonomic Seating',
            'description': 'Adjustable comfortable seating system designed for optimal steam therapy experience and user comfort',
            'icon': 'fas fa-chair',
            'order': 2
        },
        {
            'title': 'Integrated Steam System',
            'description': 'Advanced steam generation technology with precise temperature control for safe and effective therapy',
            'icon': 'fas fa-temperature-high',
            'order': 3
        },
        {
            'title': 'Easy Maintenance',
            'description': 'Non-porous smooth surfaces and quality materials make cleaning simple, quick, and hygienic',
            'icon': 'fas fa-broom',
            'order': 4
        },
        {
            'title': 'Space Efficient',
            'description': 'Compact design that fits easily in homes, clinics, and wellness centers without taking too much space',
            'icon': 'fas fa-compress',
            'order': 5
        },
        {
            'title': 'Safety Features',
            'description': 'Built-in safety mechanisms including automatic shutoff and temperature regulation for worry-free use',
            'icon': 'fas fa-lock',
            'order': 6
        }
    ]

    for feature_data in features_data:
        feature = Feature.objects.create(
            product=product,
            **feature_data
        )
        print(f"   ✓ Added feature: {feature.title}")

    # Add additional product images
    print("\n4. Adding Product Image Gallery...")
    additional_images = [
        {'image': 'products/svedapod-2.png', 'alt_text': 'SvedaPod Classic Side View', 'order': 1},
        {'image': 'products/hero-image.png', 'alt_text': 'SvedaPod Classic in Use', 'order': 2},
    ]

    for img_data in additional_images:
        if os.path.exists(f'media/{img_data["image"]}'):
            img = ProductImage.objects.create(
                product=product,
                **img_data
            )
            print(f"   ✓ Added gallery image: {img.alt_text}")
else:
    print(f"   - Product already exists: {product.name}")

# Create Testimonials
print("\n5. Creating Customer Testimonials...")
testimonials_data = [
    {
        'name': 'Dr. Priya Sharma',
        'role': 'Ayurvedic Practitioner',
        'company': 'Wellness Center, Mumbai',
        'content': 'The SvedaPod Classic has been a game-changer for our wellness center. Our clients love the authentic steam therapy experience, and the build quality is exceptional. The FRP construction is hygienic and easy to maintain. Highly recommended for any professional setting.',
        'rating': 5
    },
    {
        'name': 'Rajesh Kumar',
        'role': 'Fitness Enthusiast',
        'company': '',
        'content': 'I installed the SvedaPod in my home gym 6 months ago, and it has become an essential part of my daily routine. The stress relief and detoxification benefits are incredible. The ergonomic design makes every session comfortable. Worth every penny!',
        'rating': 5
    },
    {
        'name': 'Anita Desai',
        'role': 'Spa Owner',
        'company': 'Serenity Spa, Delhi',
        'content': 'We purchased three units for our spa, and they have been performing flawlessly for over a year. The clients appreciate the comfort and effectiveness of the steam therapy. Great product from an Indian company! The customer support has also been excellent.',
        'rating': 5
    },
    {
        'name': 'Vikram Singh',
        'role': 'Yoga Instructor',
        'company': 'Zen Yoga Studio, Bangalore',
        'content': 'As a yoga instructor, I understand the importance of holistic wellness. The SvedaPod Classic perfectly complements our yoga sessions. My students love using it after practice for relaxation and detoxification. The quality is outstanding.',
        'rating': 5
    },
    {
        'name': 'Meera Patel',
        'role': 'Health & Wellness Consultant',
        'company': '',
        'content': 'I recommend SvedaPod to all my clients looking for home wellness solutions. The Ayurvedic steam therapy has helped many with respiratory issues, stress, and overall wellbeing. The product is well-made and delivers consistent results.',
        'rating': 5
    },
    {
        'name': 'Dr. Arjun Reddy',
        'role': 'Physiotherapist',
        'company': 'Recovery Clinic, Chennai',
        'content': 'We use SvedaPod in our physiotherapy clinic for pain management and recovery. Patients report significant improvement in muscle relaxation and pain relief. The steam therapy complements our treatment protocols perfectly.',
        'rating': 5
    }
]

for testimonial_data in testimonials_data:
    testimonial, created = Testimonial.objects.get_or_create(
        name=testimonial_data['name'],
        defaults=testimonial_data
    )
    if created:
        print(f"   ✓ Created testimonial: {testimonial.name}")
    else:
        print(f"   - Already exists: {testimonial.name}")

print("\n" + "="*60)
print("✅ Data Loading Complete!")
print("="*60)
print("\nSummary:")
print(f"  • {Benefit.objects.count()} health benefits")
print(f"  • {Product.objects.count()} product(s)")
print(f"  • {Feature.objects.count()} product features")
print(f"  • {ProductImage.objects.count()} product images")
print(f"  • {Testimonial.objects.count()} customer testimonials")
print("\nNext Steps:")
print("  1. Create superuser: python manage.py createsuperuser")
print("  2. Start server: python manage.py runserver")
print("  3. Visit: http://127.0.0.1:8000")
print("  4. Admin: http://127.0.0.1:8000/admin")
print("\n✨ Your website is ready with products and images! ✨")
