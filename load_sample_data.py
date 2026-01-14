"""
Sample Data Loader for Intelpod Website
Run this script to populate your database with sample data
Usage: python manage.py shell < load_sample_data.py
"""

from products.models import Product, Benefit, Testimonial, Feature
from django.utils.text import slugify

print("Loading sample data for Intelpod website...")

# Create Benefits
benefits_data = [
    {
        'title': 'Detoxification',
        'description': 'Removes toxins from your body through natural sweating process',
        'icon': 'fas fa-droplet',
        'order': 1
    },
    {
        'title': 'Stress Relief',
        'description': 'Reduces stress and promotes relaxation for mental wellness',
        'icon': 'fas fa-heart',
        'order': 2
    },
    {
        'title': 'Respiratory Health',
        'description': 'Improves respiratory function and clears airways',
        'icon': 'fas fa-lungs',
        'order': 3
    },
    {
        'title': 'Skin Rejuvenation',
        'description': 'Enhances skin health and promotes natural glow',
        'icon': 'fas fa-spa',
        'order': 4
    },
    {
        'title': 'Weight Management',
        'description': 'Aids in weight loss and improves metabolism',
        'icon': 'fas fa-weight-scale',
        'order': 5
    },
    {
        'title': 'Pain Relief',
        'description': 'Alleviates muscle and joint pain naturally',
        'icon': 'fas fa-hand-holding-medical',
        'order': 6
    }
]

print("Creating benefits...")
for benefit_data in benefits_data:
    benefit, created = Benefit.objects.get_or_create(
        title=benefit_data['title'],
        defaults=benefit_data
    )
    if created:
        print(f"  ✓ Created benefit: {benefit.title}")
    else:
        print(f"  - Benefit already exists: {benefit.title}")

# Create Sample Product
product_data = {
    'name': 'SvedaPod Classic',
    'slug': 'svedapod-classic',
    'description': '''The SvedaPod Classic is our flagship steam bath cabinet, designed to bring the authentic Ayurvedic steam therapy experience to your home or wellness center.

Crafted with premium FRP (Fiber Reinforced Plastic) material, this cabinet offers exceptional durability, hygiene, and ease of maintenance. The ergonomic design ensures maximum comfort during your steam sessions, while the adjustable seating accommodates users of various heights.

Perfect for:
- Home wellness enthusiasts
- Ayurvedic centers
- Spas and wellness clinics
- Yoga studios
- Rehabilitation centers

The integrated steam generation system provides consistent, therapeutic steam that helps with detoxification, stress relief, respiratory health, and overall wellness. With its modern design and traditional benefits, the SvedaPod Classic is your gateway to holistic health.''',
    'short_description': 'Premium FRP steam bath cabinet with ergonomic design and integrated steam technology',
    'price': 45000.00,
    'original_price': 50000.00,
    'stock': 10,
    'available': True,
    'height': '140 cm',
    'length': '135 cm',
    'width': '75 cm',
    'material': 'FRP (Fiber Reinforced Plastic)',
    'meta_title': 'SvedaPod Classic - Premium Steam Bath Cabinet | Intelpod',
    'meta_description': 'Buy SvedaPod Classic steam bath cabinet. Made with premium FRP, ergonomic design, perfect for home and professional use. Made in India.'
}

print("\nCreating product...")
product, created = Product.objects.get_or_create(
    slug=product_data['slug'],
    defaults=product_data
)
if created:
    print(f"  ✓ Created product: {product.name}")

    # Add features to the product
    features_data = [
        {
            'title': 'Premium FRP Construction',
            'description': 'Made with high-quality Fiber Reinforced Plastic for durability and hygiene',
            'icon': 'fas fa-shield-alt',
            'order': 1
        },
        {
            'title': 'Ergonomic Seating',
            'description': 'Adjustable comfortable seating designed for optimal steam therapy experience',
            'icon': 'fas fa-chair',
            'order': 2
        },
        {
            'title': 'Integrated Steam System',
            'description': 'Advanced steam generation technology with temperature control',
            'icon': 'fas fa-temperature-high',
            'order': 3
        },
        {
            'title': 'Easy Maintenance',
            'description': 'Smooth surfaces and quality materials make cleaning simple and quick',
            'icon': 'fas fa-broom',
            'order': 4
        }
    ]

    print("  Adding product features...")
    for feature_data in features_data:
        feature = Feature.objects.create(
            product=product,
            **feature_data
        )
        print(f"    ✓ Added feature: {feature.title}")
else:
    print(f"  - Product already exists: {product.name}")

# Create Testimonials
testimonials_data = [
    {
        'name': 'Dr. Priya Sharma',
        'role': 'Ayurvedic Practitioner',
        'company': 'Wellness Center, Mumbai',
        'content': 'The SvedaPod Classic has been a game-changer for our wellness center. Our clients love the authentic steam therapy experience, and the build quality is exceptional. Highly recommended for any professional setting.',
        'rating': 5
    },
    {
        'name': 'Rajesh Kumar',
        'role': 'Fitness Enthusiast',
        'content': 'I installed the SvedaPod in my home gym 6 months ago, and it has become an essential part of my daily routine. The stress relief and detoxification benefits are incredible. Worth every penny!',
        'rating': 5
    },
    {
        'name': 'Anita Desai',
        'role': 'Spa Owner',
        'company': 'Serenity Spa, Delhi',
        'content': 'We purchased three units for our spa, and they have been performing flawlessly. The clients appreciate the comfort and effectiveness. Great product from an Indian company!',
        'rating': 5
    },
    {
        'name': 'Vikram Singh',
        'role': 'Yoga Instructor',
        'content': 'As a yoga instructor, I understand the importance of holistic wellness. The SvedaPod Classic perfectly complements our yoga sessions. My students love using it after practice.',
        'rating': 5
    }
]

print("\nCreating testimonials...")
for testimonial_data in testimonials_data:
    testimonial, created = Testimonial.objects.get_or_create(
        name=testimonial_data['name'],
        defaults=testimonial_data
    )
    if created:
        print(f"  ✓ Created testimonial from: {testimonial.name}")
    else:
        print(f"  - Testimonial already exists from: {testimonial.name}")

print("\n" + "="*50)
print("Sample data loading complete!")
print("="*50)
print("\nYou can now:")
print("1. Visit http://127.0.0.1:8000 to see your website")
print("2. Go to http://127.0.0.1:8000/admin to manage content")
print("3. Add product images through the admin panel")
print("\nNote: Product images need to be uploaded manually through admin.")
