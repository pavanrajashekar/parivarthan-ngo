from django.shortcuts import render
from .models import Program

def programs_list(request):
    context = {
        'programs': Program.objects.all()
    }
    return render(request, 'programs/programs.html', context)
