from django.shortcuts import render
from .models import Blog
from donations.models import SponsorshipPlan

def home(request):
    # Fetch all blogs from database, ordered by latest
    context = {
        'posts': Blog.objects.all().order_by('-date_posted'),
        'plans': SponsorshipPlan.objects.all()
    }
    return render(request, 'blog/home.html', context)
