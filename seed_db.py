import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parivarthan.settings')
django.setup()

from programs.models import Program
from donations.models import SponsorshipPlan

def seed():
    # Only seed if database is completely empty (i.e. fresh deployment)
    if not Program.objects.exists():
        print("Empty database detected. Injecting authentic Parivarthan Programs...")
        Program.objects.create(
            name='Special School for the Hearing Impaired',
            description='Providing specialized education and a barrier-free inclusive environment for hearing-impaired children.',
            location='Eluru, Andhra Pradesh'
        )
        Program.objects.create(
            name='Clinical Assessment',
            description='Need-based comprehensive rehabilitation and early clinical assessment for children with different abilities.',
            location='Eluru, Andhra Pradesh'
        )
        Program.objects.create(
            name='Comprehensive Rehabilitation',
            description='A multi-disciplinary approach to ensure empowerment to persons with different abilities and their families.',
            location='Eluru, Andhra Pradesh'
        )

    if not SponsorshipPlan.objects.exists():
        print("Empty database detected. Injecting authentic Parivarthan Sponsorship Plans...")
        SponsorshipPlan.objects.create(
            title='Sponsor a Special Education Kit',
            description='Provide specialized learning materials and tools for a hearing-impaired student.',
            amount=1000
        )
        SponsorshipPlan.objects.create(
            title='Speech Therapy Sessions',
            description='Fund one month of intensive, professional speech therapy for a child to build essential communication skills.',
            amount=5000
        )
        SponsorshipPlan.objects.create(
            title='Sponsor a Hearing Aid',
            description='Provide a high-quality hearing aid instrument to profoundly change a child’s interaction with the world.',
            amount=10000
        )

    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        print("No superuser found. Creating default superuser...")
        User.objects.create_superuser(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@parivarthan.org'),
            password=os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
        )


if __name__ == '__main__':
    seed()
    print("Database seeding verification complete.")
