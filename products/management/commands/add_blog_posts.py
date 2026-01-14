from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import BlogPost
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Add blog posts from intelpod.in to the database'

    def handle(self, *args, **kwargs):
        # Get or create default author (admin user)
        admin_user = User.objects.filter(is_superuser=True).first()
        if not admin_user:
            # If no admin exists, try to get first user
            admin_user = User.objects.first()
            if not admin_user:
                self.stdout.write(self.style.ERROR('No users found. Please create a user first.'))
                return

        blog_posts = [
            {
                'slug': 'how-a-steam-bath-cabinet-can-improve-your-sleep-quality',
                'title': 'How a Steam Bath Cabinet Can Improve Your Sleep Quality',
                'excerpt': "In today's fast-paced world, achieving quality sleep is becoming increasingly difficult for many people. Stress, anxiety, and physical discomfort are some of the most common barriers to a good night's rest.",
                'content': """<p>In today's fast-paced world, achieving quality sleep is becoming increasingly difficult for many people. Stress, anxiety, and physical discomfort are some of the most common barriers to a good night's rest. If you struggle with sleep issues, incorporating a steam bath cabinet into your wellness routine could be the natural solution you've been looking for.</p>

<h2>Relaxation and Stress Relief</h2>
<p>The soothing heat of a steam bath triggers the release of endorphins, your body's natural "feel-good" hormones. This helps reduce tension and anxiety that often prevent restful sleep. By creating a calm, tranquil environment, steam therapy helps your mind and body prepare for deep, restorative rest.</p>

<h2>Improved Circulation</h2>
<p>Steam causes blood vessels to dilate, enhancing oxygen delivery throughout your body. This improved circulation promotes a sense of calm and relaxation, making it easier to drift off to sleep naturally.</p>

<h2>Temperature Regulation</h2>
<p>When you use a steam bath, your body temperature rises during the session. Afterward, as your body cools down, it mimics the natural temperature drop that occurs before sleep. This process signals to your brain that it's time to rest, facilitating faster sleep onset.</p>

<h2>Calming the Nervous System</h2>
<p>Heat therapy has been shown to reduce cortisol levels—the stress hormone that keeps you alert and anxious. By lowering cortisol, steam baths create mental and physical tranquility, setting the stage for better sleep quality.</p>

<h2>Respiratory Benefits</h2>
<p>The moist, warm air in a steam bath opens your airways, making breathing easier. This is especially beneficial for those with allergies, asthma, or sinus congestion that can disrupt sleep. Clearer breathing means more restful, uninterrupted sleep throughout the night.</p>

<h2>Creating a Bedtime Ritual</h2>
<p>Using a steam bath cabinet as part of your evening routine signals to your body that it's time to wind down. Establishing this consistent pre-sleep ritual can train your brain to recognize that relaxation and rest are coming, making it easier to fall asleep naturally.</p>

<h2>Conclusion</h2>
<p>Steam bath cabinets offer several benefits that can significantly improve your sleep quality through combined physical relaxation, enhanced circulation, stress reduction, and respiratory improvements. If you're looking for a natural way to enhance your sleep, a steam bath might be exactly what you need.</p>""",
                'featured_image': 'blog/blog-1-sleep-quality.png',
                'meta_description': 'Discover how steam bath cabinets can naturally improve your sleep quality through relaxation, stress relief, and better circulation.',
            },
            {
                'slug': 'the-science-behind-steam-baths-how-they-help-detoxify-your-body',
                'title': 'The Science Behind Steam Baths: How They Help Detoxify Your Body',
                'excerpt': 'Steam baths have been a cornerstone of wellness practices for centuries, from ancient Roman baths to modern-day spas. Today, steam bath cabinets are gaining popularity as convenient home wellness devices.',
                'content': """<p>Steam baths have been a cornerstone of wellness practices for centuries, from ancient Roman baths to modern-day spas. Today, steam bath cabinets are gaining popularity as convenient home wellness devices. But how exactly does steam therapy facilitate bodily detoxification?</p>

<h2>Sweating and Toxin Release</h2>
<p>When you sit in a steam bath, the heat causes your pores to open and triggers perspiration. Sweating is one of the body's primary methods for eliminating toxins, including heavy metals, chemicals, pollutants, and excess salts. As you sweat, these harmful substances are expelled through your skin, helping to cleanse your system naturally.</p>

<h2>Enhanced Circulation</h2>
<p>The warmth from steam causes your blood vessels to expand, significantly improving blood flow throughout your body. This enhanced circulation means that more oxygen and nutrients reach your vital organs—including your liver, kidneys, and lymphatic system—supporting their natural detoxification functions. Better circulation also helps transport toxins to elimination pathways more efficiently.</p>

<h2>Deep Skin Cleansing</h2>
<p>Steam opens your pores deeply, allowing trapped dirt, oil, and impurities to be released. This deep cleansing effect can reduce breakouts, congestion, and improve your skin's overall health and appearance. Clean pores mean fewer toxins are absorbed back into your body through your skin.</p>

<h2>Stress Reduction and Cortisol Management</h2>
<p>The calming environment of a steam bath helps lower cortisol levels, your body's primary stress hormone. High cortisol can impair your body's natural detoxification processes. By creating a tranquil space for relaxation, steam therapy helps restore balance and enhances your body's ability to cleanse itself.</p>

<h2>Lymphatic System Support</h2>
<p>The heat from steam therapy encourages lymphatic fluid movement, which is essential for waste removal from your cells. A well-functioning lymphatic system is crucial for detoxification, immune health, and overall wellness.</p>

<h2>Conclusion</h2>
<p>Steam baths work as effective detoxification tools through a combination of sweating, improved circulation, deep skin cleansing, and lymphatic drainage. By supporting your body's innate cleaning mechanisms, regular steam therapy can help you feel healthier, more energized, and rejuvenated.</p>""",
                'featured_image': 'blog/blog-2-detoxify.png',
                'meta_description': 'Learn the science behind how steam baths help detoxify your body through sweating, circulation, and lymphatic system support.',
            },
            {
                'slug': 'the-future-of-home-wellness-steam-bath-cabinets-for-every-household',
                'title': 'The Future of Home Wellness: Steam Bath Cabinets for Every Household',
                'excerpt': "As the world becomes more health-conscious and prioritizes wellness, the demand for home spa experiences has grown significantly. Steam bath cabinets are at the forefront of this transformation.",
                'content': """<p>As the world becomes more health-conscious and prioritizes wellness, the demand for home spa experiences has grown significantly. Steam bath cabinets are increasingly becoming accessible wellness products that transform how people experience relaxation and self-care at home.</p>

<h2>The Wellness Revolution in India</h2>
<p>India has particularly embraced this wellness trend, connecting modern steam cabinets to traditional Ayurvedic wellness practices. These units offer relaxing and rejuvenating experiences suited to contemporary urban lifestyles while maintaining cultural wellness traditions. For busy professionals seeking accessible self-care without spa visits, steam bath cabinets are becoming essential home wellness features.</p>

<h2>Global Wellness Trends</h2>
<p>The popularity of home steam bath cabinets is growing across multiple regions:</p>

<h3>United States</h3>
<p>Rising adoption in residential settings as part of daily wellness routines, with homeowners recognizing the long-term health benefits of regular steam therapy.</p>

<h3>Europe</h3>
<p>Expansion from public spas to private homes is particularly strong in Germany and Switzerland, where wellness culture is deeply embedded in lifestyle.</p>

<h3>Asia</h3>
<p>Growing demand in Japan and South Korea builds on established steam and sauna traditions, with modern cabinets offering convenience and space efficiency.</p>

<h2>Health Benefits Driving Adoption</h2>
<ul>
<li><strong>Improved Circulation:</strong> Regular steam sessions enhance blood flow and cardiovascular health</li>
<li><strong>Detoxification:</strong> Natural elimination of toxins through perspiration</li>
<li><strong>Enhanced Skin Health:</strong> Deep hydration and improved complexion</li>
<li><strong>Stress Relief:</strong> Mental relaxation and tension reduction</li>
<li><strong>Respiratory Support:</strong> Relief from congestion and breathing difficulties</li>
</ul>

<h2>Lifestyle Integration</h2>
<p>Modern steam bath cabinets are designed for easy integration into home bathrooms, offering convenience for those seeking accessible self-care. These personal wellness sanctuaries provide spa-quality experiences without leaving home, saving time and money while promoting consistent wellness habits.</p>

<h2>The Future Outlook</h2>
<p>Steam bath cabinets are projected to become standard home wellness features, particularly across India and globally. As more people prioritize preventive health care and mental wellness, the demand for convenient, effective home wellness solutions will continue to rise.</p>

<h2>Conclusion</h2>
<p>The future of home wellness includes steam bath cabinets in every household, creating a healthier and more relaxed world, one steam bath at a time. This transformation represents not just a trend, but a fundamental shift in how people approach daily wellness and self-care.</p>""",
                'featured_image': 'blog/blog-3-future-wellness.png',
                'meta_description': 'Explore how steam bath cabinets are becoming essential home wellness features worldwide, transforming daily self-care routines.',
            },
            {
                'slug': 'why-steam-bath-cabinets-are-the-secret-to-better-skin',
                'title': 'Why Steam Bath Cabinets Are the Secret to Better Skin',
                'excerpt': 'A steam bath cabinet is not only a great way to relax and unwind but also an excellent tool for improving the health and appearance of your skin.',
                'content': """<p>A steam bath cabinet is not only a great way to relax and unwind but also an excellent tool for improving the health and appearance of your skin. Discover how regular steam therapy can transform your complexion and give you glowing, healthy skin.</p>

<h2>Deep Cleansing for Clear Skin</h2>
<p>Steam opens your pores thoroughly, removing trapped dirt, oil, and impurities that accumulate throughout the day. This deep cleansing prevents clogged pores that can trigger breakouts and acne. By regularly using a steam bath, you maintain cleaner pores and clearer skin naturally.</p>

<h2>Improved Circulation and Radiance</h2>
<p>The heat from steam therapy increases blood flow to your skin cells, delivering more oxygen and nutrients exactly where they're needed. This enhanced circulation promotes a healthier complexion and creates that natural, youthful radiance everyone desires. Better blood flow also means faster skin cell regeneration and repair.</p>

<h2>Intense Hydration</h2>
<p>Steam encourages moisture retention in your skin while opening pores, making it particularly beneficial for dry or dehydrated skin. The added hydration plumps your skin, reducing the appearance of fine lines and wrinkles. Well-hydrated skin looks smoother, softer, and more supple.</p>

<h2>Detoxification for Clearer Complexion</h2>
<p>Sweating during steam sessions releases toxins through your skin, helping clear imperfections and improve overall skin texture. As your body eliminates waste products through perspiration, your skin becomes clearer, brighter, and more even-toned.</p>

<h2>Stress Reduction for Healthier Skin</h2>
<p>The tranquil environment of a steam bath helps manage stress, which is a major contributor to skin problems like acne, eczema, and premature aging. By balancing hormone levels and reducing cortisol, steam therapy helps prevent stress-related skin issues and maintains a healthy, youthful appearance.</p>

<h2>Enhanced Product Absorption</h2>
<p>After a steam session, your open pores become more receptive to skincare products. Serums, moisturizers, and treatments penetrate deeper and work more effectively, maximizing the benefits of your skincare routine. This means you get more value from your skincare products.</p>

<h2>Natural Anti-Aging Benefits</h2>
<p>Regular steam therapy stimulates collagen production, which is essential for maintaining skin elasticity and firmness. This natural anti-aging effect helps reduce wrinkles, fine lines, and sagging, keeping your skin looking younger and more vibrant over time.</p>

<h2>Conclusion</h2>
<p>Steam bath cabinets are a fantastic way to nourish and revitalize your skin naturally, offering the rejuvenating effects of a spa treatment right in the comfort of your own home. With consistent use, you'll notice clearer, smoother, more radiant skin that reflects your inner health and wellness.</p>""",
                'featured_image': 'blog/blog-4-better-skin.png',
                'meta_description': 'Discover why steam bath cabinets are the secret to better skin through deep cleansing, hydration, and improved circulation.',
            },
            {
                'slug': 'the-ultimate-guide-to-choosing-the-best-steam-bath-cabinet-for-your-home',
                'title': 'The Ultimate Guide to Choosing the Best Steam Bath Cabinet for Your Home',
                'excerpt': "A steam bath is more than just a luxurious addition to your home; it's an investment in wellness, relaxation, and overall health.",
                'content': """<p>A steam bath is more than just a luxurious addition to your home; it's an investment in wellness, relaxation, and overall health. Choosing the right steam bath cabinet can transform your bathroom into a personal spa that offers stress relief and numerous health benefits for years to come.</p>

<h2>Material Selection: Why FRP is Superior</h2>
<p>When selecting a steam bath cabinet, material choice is crucial. Fiber Reinforced Plastic (FRP) stands out as the superior option compared to traditional materials like wood or acrylic. Here's why:</p>

<ul>
<li><strong>Moisture Resistance:</strong> FRP is naturally resistant to water damage, preventing warping, rotting, or deterioration even with daily use</li>
<li><strong>Non-Porous Surface:</strong> Unlike wood, FRP doesn't absorb moisture, preventing mold and mildew growth</li>
<li><strong>Durability:</strong> FRP cabinets maintain their shape and functionality for many years, outlasting wood alternatives</li>
<li><strong>Low Maintenance:</strong> Easy to clean with just mild cleaners and a soft cloth</li>
<li><strong>Aesthetic Versatility:</strong> Available in various finishes and colors to match your bathroom décor</li>
</ul>

<h2>Size and Design Considerations</h2>
<p>Before purchasing, carefully measure your bathroom space to ensure proper fit. Consider these factors:</p>

<h3>Space Requirements</h3>
<p>Ensure adequate clearance around the cabinet for entry, exit, and ventilation. Standard sizes range from compact single-person units to larger family-sized models.</p>

<h3>Design Features to Look For</h3>
<ul>
<li><strong>Ergonomic Seating:</strong> Comfortable built-in benches or seats for extended sessions</li>
<li><strong>Customizable Finishes:</strong> Options that complement your bathroom style</li>
<li><strong>Ambient Lighting:</strong> Built-in LED lighting for relaxation</li>
<li><strong>Temperature Controls:</strong> Easy-to-use digital controls for precise temperature management</li>
<li><strong>Steam Generator Quality:</strong> Reliable, efficient steam production system</li>
</ul>

<h2>Durability and Long-Term Performance</h2>
<p>Investing in quality pays off over time. FRP cabinets excel in longevity:</p>

<ul>
<li>Resistant to daily wear and humidity exposure</li>
<li>No warping or cracking like wood alternatives</li>
<li>Color and finish remain vibrant for years</li>
<li>Structural integrity maintained even with frequent use</li>
</ul>

<h2>Maintenance and Care</h2>
<p>One of FRP's greatest advantages is minimal maintenance requirements:</p>

<ul>
<li>Quick wipe-down after each use keeps it pristine</li>
<li>No special treatments or sealants needed</li>
<li>Resistant to common bathroom cleaning products</li>
<li>No refinishing or resealing required over the years</li>
</ul>

<h2>Budget Considerations</h2>
<p>While initial costs for quality FRP steam bath cabinets may be higher than budget alternatives, consider the long-term value:</p>

<ul>
<li><strong>Longevity:</strong> Years of reliable use without replacement</li>
<li><strong>Minimal Repairs:</strong> Reduced maintenance costs over time</li>
<li><strong>Energy Efficiency:</strong> Modern steam generators are cost-effective to operate</li>
<li><strong>Home Value:</strong> Adds significant value to your property</li>
<li><strong>Health Savings:</strong> Reduced stress and improved wellness may lower healthcare costs</li>
</ul>

<h2>Installation Considerations</h2>
<p>Professional installation ensures optimal performance:</p>

<ul>
<li>Proper electrical connections for steam generator</li>
<li>Adequate ventilation to prevent moisture buildup in bathroom</li>
<li>Waterproofing around installation area</li>
<li>Drain access for condensation</li>
</ul>

<h2>Additional Features to Consider</h2>
<p>Modern steam bath cabinets offer various enhanced features:</p>

<ul>
<li><strong>Aromatherapy Systems:</strong> Built-in dispensers for essential oils</li>
<li><strong>Audio Systems:</strong> Bluetooth speakers for relaxing music</li>
<li><strong>Chromotherapy Lighting:</strong> Color therapy through LED lights</li>
<li><strong>Digital Controls:</strong> Smartphone app integration for remote operation</li>
<li><strong>Safety Features:</strong> Automatic shut-off and temperature limiters</li>
</ul>

<h2>Choosing the Right Brand</h2>
<p>Select manufacturers with:</p>

<ul>
<li>Proven track record in steam bath technology</li>
<li>Comprehensive warranty coverage</li>
<li>Responsive customer service</li>
<li>Quality certifications and safety standards compliance</li>
<li>Positive customer reviews and testimonials</li>
</ul>

<h2>Conclusion</h2>
<p>Choosing the best steam bath cabinet for your home involves balancing material quality, size, design, maintenance ease, and budget. FRP steam bath cabinets offer the optimal combination of durability, low maintenance, and aesthetic appeal, making them an excellent choice for creating your personal wellness sanctuary.</p>

<p>By investing in a quality steam bath cabinet, you're not just adding a bathroom fixture—you're creating a daily wellness ritual that promotes relaxation, health, and rejuvenation for years to come.</p>""",
                'featured_image': 'blog/blog-5-choosing-guide.png',
                'meta_description': 'Complete guide to choosing the best steam bath cabinet for your home. Learn about materials, features, and what to look for.',
            },
        ]

        for post_data in blog_posts:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    'title': post_data['title'],
                    'excerpt': post_data['excerpt'],
                    'content': post_data['content'],
                    'featured_image': post_data['featured_image'],
                    'meta_description': post_data['meta_description'],
                    'author': admin_user,
                    'published': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added: {post_data["title"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'- Already exists: {post_data["title"]}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Blog posts import completed!'))
