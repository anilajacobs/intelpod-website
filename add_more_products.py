"""
Add More Products with Images
Run: python manage.py shell < add_more_products.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelpod_website.settings')
django.setup()

from products.models import Product, Feature, ProductImage
from django.utils.text import slugify

print("="*70)
print("Adding More Products to Intelpod Website")
print("="*70)

# Product 2: SvedaPod Premium
print("\n1. Creating SvedaPod Premium...")
product2_data = {
    'name': 'SvedaPod Premium',
    'slug': 'svedapod-premium',
    'description': '''The SvedaPod Premium is our enhanced steam bath cabinet, featuring advanced amenities and superior comfort for the discerning wellness enthusiast.

**Premium Features**
Building upon the solid foundation of our Classic model, the Premium edition incorporates upgraded materials, enhanced ergonomics, and additional comfort features. The cabinet features a reinforced FRP construction with a luxurious finish that complements any high-end wellness facility or upscale home.

**Enhanced Comfort**
The Premium model includes padded seating with memory foam comfort, adjustable headrest, built-in aromatherapy diffuser, and LED mood lighting. The spacious interior provides extra room for a more relaxed and luxurious steam experience.

**Advanced Controls**
Equipped with a digital control panel that allows precise temperature and duration settings. The intuitive interface makes it easy to customize your steam therapy sessions. Pre-programmed wellness routines for different health goals are included.

**Superior Steam System**
Features an upgraded steam generator with faster heat-up time and more consistent steam distribution. The system includes automatic water level sensors and safety shutoff mechanisms for worry-free operation.

**Ideal For:**
- Luxury spas and wellness resorts
- High-end fitness centers and clubs
- Premium home wellness installations
- Ayurvedic therapy centers
- Executive wellness suites
- Boutique hotels and resorts

**Additional Benefits:**
The Premium model offers all the health benefits of steam therapy while providing an elevated experience with enhanced comfort, better control, and premium aesthetics. Perfect for clients who demand the best in wellness equipment.

**Quality & Support:**
Comes with extended warranty and priority customer support. Installation guidance and maintenance training included.''',
    'short_description': 'Enhanced steam bath cabinet with premium features, digital controls, aromatherapy, mood lighting, and superior comfort',
    'price': 65000.00,
    'original_price': 75000.00,
    'stock': 10,
    'available': True,
    'height': '145 cm',
    'length': '140 cm',
    'width': '80 cm',
    'material': 'Premium FRP with Reinforced Frame',
    'meta_title': 'SvedaPod Premium - Luxury Steam Bath Cabinet | Intelpod',
    'meta_description': 'Premium steam bath cabinet with digital controls, aromatherapy, LED lighting, and enhanced comfort. Perfect for luxury spas and homes.',
    'image': 'products/svedapod-premium.png'
}

product2, created = Product.objects.get_or_create(
    slug=product2_data['slug'],
    defaults=product2_data
)

if created:
    print(f"   ✓ Created: {product2.name}")

    features2 = [
        {
            'title': 'Digital Control Panel',
            'description': 'Advanced touchscreen interface for precise temperature and time control with preset programs',
            'icon': 'fas fa-tablet-alt',
            'order': 1
        },
        {
            'title': 'Aromatherapy System',
            'description': 'Built-in essential oil diffuser to enhance your steam therapy with therapeutic aromas',
            'icon': 'fas fa-seedling',
            'order': 2
        },
        {
            'title': 'LED Mood Lighting',
            'description': 'Customizable chromotherapy lighting system for enhanced relaxation and wellness',
            'icon': 'fas fa-lightbulb',
            'order': 3
        },
        {
            'title': 'Memory Foam Seating',
            'description': 'Padded comfortable seating with memory foam for extended session comfort',
            'icon': 'fas fa-couch',
            'order': 4
        },
        {
            'title': 'Premium Finish',
            'description': 'Luxury finish with reinforced construction for durability and aesthetic appeal',
            'icon': 'fas fa-gem',
            'order': 5
        },
        {
            'title': 'Advanced Safety',
            'description': 'Multiple safety features including auto-shutoff, water sensors, and temperature limiters',
            'icon': 'fas fa-shield-check',
            'order': 6
        }
    ]

    for feat in features2:
        Feature.objects.create(product=product2, **feat)
    print(f"   ✓ Added {len(features2)} features")
else:
    print(f"   - Already exists: {product2.name}")

# Product 3: SvedaPod Deluxe
print("\n2. Creating SvedaPod Deluxe...")
product3_data = {
    'name': 'SvedaPod Deluxe',
    'slug': 'svedapod-deluxe',
    'description': '''The SvedaPod Deluxe represents the pinnacle of steam therapy excellence, combining traditional Ayurvedic wisdom with cutting-edge technology and ultimate luxury.

**Ultimate Wellness Experience**
The Deluxe model is our most advanced steam cabinet, designed for those who accept nothing but the best. Every aspect has been carefully engineered to provide an unparalleled wellness experience that rivals the finest spa destinations.

**Luxury Materials & Construction**
Constructed with premium-grade FRP reinforced with a titanium-alloy frame for maximum durability. The interior features medical-grade stainless steel fittings and antimicrobial coating that ensures the highest standards of hygiene.

**Smart Technology Integration**
Features IoT connectivity with smartphone app control, allowing you to start, monitor, and customize your sessions remotely. Voice control compatibility with major smart home systems. Automated maintenance alerts and diagnostics.

**Professional-Grade Steam System**
Hospital-grade steam generation system with multi-zone steam distribution for uniform coverage. Advanced filtration system ensures pure, therapeutic steam. Rapid heat-up technology gets you started in minutes.

**Sensory Enhancement**
- Premium Bose sound system for music or guided meditation
- Chromotherapy lighting with multiple preset programs
- Automated aromatherapy with oil reservoir for 20+ sessions
- Ionized air circulation system
- Built-in meditation timer with gentle alerts

**Therapeutic Features**
- Separate controls for upper and lower body steam zones
- Pulse-wave massage function through vibrating back support
- Ozone therapy option for enhanced detoxification
- Himalayan salt therapy integration
- Infrared heating panels for deeper tissue penetration

**Perfect For:**
- Five-star hotel spa facilities
- Medical wellness clinics
- Premium rehabilitation centers
- Executive health clubs
- Celebrity and VIP home installations
- Luxury resort spa suites

**Dimensions & Specifications**
Larger interior with premium space allocation. Reinforced glass door with heated anti-fog coating. Wheelchair accessible entry option available.

**Installation & Warranty**
Includes white-glove installation service, comprehensive training, and 5-year extended warranty. 24/7 priority support hotline.

**The Ultimate Investment**
The Deluxe model is more than a steam cabinet – it's a complete wellness sanctuary that delivers therapeutic benefits while providing an luxurious experience that exceeds expectations.''',
    'short_description': 'Ultimate luxury steam cabinet with IoT connectivity, app control, Bose sound system, chromotherapy, and professional-grade features',
    'price': 125000.00,
    'original_price': 150000.00,
    'stock': 5,
    'available': True,
    'height': '150 cm',
    'length': '145 cm',
    'width': '85 cm',
    'material': 'Premium FRP with Titanium-Alloy Frame',
    'meta_title': 'SvedaPod Deluxe - Ultimate Luxury Steam Cabinet | Intelpod',
    'meta_description': 'Top-of-the-line steam cabinet with smart controls, Bose audio, chromotherapy, and professional spa features. The ultimate wellness investment.',
    'image': 'products/svedapod-deluxe.png'
}

product3, created = Product.objects.get_or_create(
    slug=product3_data['slug'],
    defaults=product3_data
)

if created:
    print(f"   ✓ Created: {product3.name}")

    features3 = [
        {
            'title': 'IoT Smart Control',
            'description': 'Smartphone app control with remote start, monitoring, and customization capabilities',
            'icon': 'fas fa-mobile-alt',
            'order': 1
        },
        {
            'title': 'Bose Sound System',
            'description': 'Premium audio system for music, meditation, or guided wellness programs',
            'icon': 'fas fa-music',
            'order': 2
        },
        {
            'title': 'Multi-Zone Steam',
            'description': 'Separate upper and lower body steam controls for targeted therapy',
            'icon': 'fas fa-layer-group',
            'order': 3
        },
        {
            'title': 'Chromotherapy Plus',
            'description': 'Advanced LED color therapy with preset programs and custom sequences',
            'icon': 'fas fa-palette',
            'order': 4
        },
        {
            'title': 'Pulse-Wave Massage',
            'description': 'Integrated vibration massage system for enhanced muscle relaxation',
            'icon': 'fas fa-hand-sparkles',
            'order': 5
        },
        {
            'title': 'Premium Materials',
            'description': 'Titanium-alloy frame, medical-grade steel fittings, antimicrobial surfaces',
            'icon': 'fas fa-star',
            'order': 6
        }
    ]

    for feat in features3:
        Feature.objects.create(product=product3, **feat)
    print(f"   ✓ Added {len(features3)} features")
else:
    print(f"   - Already exists: {product3.name}")

# Product 4: SvedaPod Commercial
print("\n3. Creating SvedaPod Commercial...")
product4_data = {
    'name': 'SvedaPod Commercial Pro',
    'slug': 'svedapod-commercial-pro',
    'description': '''The SvedaPod Commercial Pro is specifically engineered for high-traffic commercial environments, delivering reliable performance day after day.

**Built for Business**
Designed with commercial durability in mind, the Commercial Pro model can handle continuous daily use in busy spa, gym, and wellness center environments. Industrial-grade components ensure longevity and minimal downtime.

**Heavy-Duty Construction**
Features reinforced FRP construction with steel support structure rated for 500+ sessions per month. Commercial-grade hinges, seals, and door mechanisms built to withstand frequent opening and closing. Scratch-resistant exterior coating.

**High-Performance Steam System**
Industrial steam generator with 30% faster recovery time between sessions. Designed for back-to-back use with minimal wait time. Large capacity water reservoir reduces refill frequency. Quick-drain system for easy cleaning between clients.

**Easy Maintenance**
Removable panels for easy access to all components. Tool-free filter changes. Self-cleaning steam nozzles. Diagnostic system alerts staff to maintenance needs before problems occur. All parts readily available with next-day shipping.

**Hygiene Features**
Antimicrobial surfaces throughout. UV sanitization system option. Easy-clean textured flooring. Removable seat cushions that can be sanitized. Built-in ventilation system prevents moisture buildup.

**Business-Friendly Features**
- Usage counter tracks total sessions and maintenance intervals
- Multi-user preset programs for different service packages
- Quick-start mode for rapid client turnover
- Energy-efficient operation reduces utility costs
- Quiet operation doesn't disturb adjacent treatment rooms

**Ideal For:**
- Day spas and wellness centers
- Gym and fitness center wet areas
- Hotel spa facilities
- Physical therapy clinics
- Corporate wellness rooms
- Medical wellness facilities
- Ayurvedic treatment centers
- Sports training facilities

**Capacity & Efficiency**
Designed to serve 15-20 clients per day reliably. Energy Star rated efficiency. Low maintenance requirements keep operating costs down. Durable construction means years of reliable service.

**Commercial Support**
Comes with commercial warranty, installation service, staff training, and ongoing technical support. Preventive maintenance packages available. Replacement unit during repairs option for critical operations.

**ROI & Value**
The Commercial Pro model pays for itself through reliable operation, minimal downtime, and satisfied clients. Built to generate revenue, not maintenance bills.

**Customization Options**
Available in multiple finishes to match your facility aesthetics. Custom branding options available. Can be networked with facility management systems.''',
    'short_description': 'Heavy-duty commercial steam cabinet built for high-traffic environments, featuring industrial-grade components and easy maintenance',
    'price': 85000.00,
    'original_price': 95000.00,
    'stock': 8,
    'available': True,
    'height': '145 cm',
    'length': '140 cm',
    'width': '80 cm',
    'material': 'Reinforced Commercial-Grade FRP',
    'meta_title': 'SvedaPod Commercial Pro - Industrial Steam Cabinet | Intelpod',
    'meta_description': 'Commercial-grade steam cabinet designed for spas, gyms, and wellness centers. Heavy-duty construction for high-traffic use.',
    'image': 'products/svedapod-commercial.png'
}

product4, created = Product.objects.get_or_create(
    slug=product4_data['slug'],
    defaults=product4_data
)

if created:
    print(f"   ✓ Created: {product4.name}")

    features4 = [
        {
            'title': 'Heavy-Duty Construction',
            'description': 'Industrial-grade materials rated for 500+ sessions per month in commercial settings',
            'icon': 'fas fa-industry',
            'order': 1
        },
        {
            'title': 'Fast Recovery Time',
            'description': '30% faster between sessions, perfect for high-traffic facilities',
            'icon': 'fas fa-bolt',
            'order': 2
        },
        {
            'title': 'Easy Maintenance',
            'description': 'Tool-free servicing with diagnostic alerts for preventive maintenance',
            'icon': 'fas fa-tools',
            'order': 3
        },
        {
            'title': 'UV Sanitization',
            'description': 'Optional UV system ensures highest hygiene standards between clients',
            'icon': 'fas fa-virus-slash',
            'order': 4
        },
        {
            'title': 'Usage Tracking',
            'description': 'Built-in counter tracks sessions and maintenance intervals for business management',
            'icon': 'fas fa-chart-line',
            'order': 5
        },
        {
            'title': 'Energy Efficient',
            'description': 'Energy Star rated operation keeps utility costs low for commercial use',
            'icon': 'fas fa-leaf',
            'order': 6
        }
    ]

    for feat in features4:
        Feature.objects.create(product=product4, **feat)
    print(f"   ✓ Added {len(features4)} features")
else:
    print(f"   - Already exists: {product4.name}")

# Summary
print("\n" + "="*70)
print("✅ Product Addition Complete!")
print("="*70)

all_products = Product.objects.all()
print(f"\nTotal Products: {all_products.count()}")
print("\nProduct List:")
for i, p in enumerate(all_products, 1):
    print(f"  {i}. {p.name}")
    print(f"     - Price: ₹{p.price:,.0f}")
    print(f"     - Stock: {p.stock} units")
    print(f"     - Features: {p.features.count()}")
    print()

print("="*70)
print("🎉 All products loaded successfully!")
print("="*70)
print("\nStart your server to see all products:")
print("  python manage.py runserver")
print("\nVisit: http://127.0.0.1:8000/products/")
print("="*70)
