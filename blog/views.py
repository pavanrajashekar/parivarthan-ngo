from django.shortcuts import render
from .models import Blog

def home(request):
    # Fetch all blogs from database, ordered by latest
    context = {
        'posts': Blog.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)
