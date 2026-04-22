from django.shortcuts import render
from .models import Blog
from donations.models import SponsorshipPlan
from programs.models import Program
from contact.forms import ContactForm

def home(request):
    # The master Data Controller for the SPA
    context = {
        'posts': Blog.objects.all().order_by('-date_posted')[:3], # Only top 3 for preview
        'plans': SponsorshipPlan.objects.all(),
        'programs': Program.objects.all()[:3], # Top 3 programs for preview
        'contact_form': ContactForm()
    }
    return render(request, 'blog/home.html', context)
