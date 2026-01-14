from django.core.management.base import BaseCommand
from products.models import TeamMember


class Command(BaseCommand):
    help = 'Add team members to the database'

    def handle(self, *args, **kwargs):
        team_data = [
            {
                'name': 'Palakeezhil Azeezkunju Noushad',
                'role': 'founder',
                'title': 'Founder',
                'bio': 'Over 35 years of experience in interior and product design. He combines design expertise with innovative wellness solutions, emphasizing that comfort and well-being are at the core of every creation. Passionate about architectural trends and creative pursuits.',
                'email': 'noushad@intelpod.in',
                'linkedin_url': '',
                'photo': 'team/noushad.png',
                'order': 1,
                'active': True,
            },
            {
                'name': 'Paakkaran',
                'role': 'ceo',
                'title': 'Co-Founder, CEO',
                'bio': 'Leads organizational strategy, operations, and growth. Brings over a decade of marketing and sales expertise in branding, market expansion, and customer engagement. Passionate about traveling and exploring different markets to better serve our customers.',
                'email': 'musthafa@intelpod.in',
                'linkedin_url': 'https://www.linkedin.com/in/muhammed-m-92a2b31b7/',
                'photo': 'team/musthafa.png',
                'order': 2,
                'active': True,
            },
            {
                'name': 'Dr. Renjith Purushothaman',
                'role': 'cto',
                'title': 'Director, CTO',
                'bio': '4th-generation Ayurveda doctor integrating ancient wellness practices with cutting-edge advancements. His deep Ayurvedic knowledge shapes our product offerings and ensures authenticity. Dedicated to natural healing and sustainable living.',
                'email': 'renjith@intelpod.in',
                'linkedin_url': '',
                'photo': 'team/renjith.png',
                'order': 3,
                'active': True,
            },
            {
                'name': 'Abraham Antony',
                'role': 'CCO',
                'title': 'Director, Chief Commercial Officer (CCO)',
                'bio': 'Oversees commercial strategy, sales growth, and digital marketing. Brings over a decade of experience in branding, market expansion, and building trusted customer relationships. Drives our mission to make wellness accessible to everyone.',
                'email': 'abraham@intelpod.in',
                'linkedin_url': 'https://www.linkedin.com/in/abrahamantony96',
                'photo': 'team/abraham.jpg',
                'order': 4,
                'active': True,
            },
        ]

        for data in team_data:
            member, created = TeamMember.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added: {data["name"]} - {data["title"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'- Already exists: {data["name"]}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Team members import completed!'))
