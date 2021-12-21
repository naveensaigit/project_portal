from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project
@login_required
def main(request):
    context = {
        'title': 'Home',
        'projects': Project.objects.all()
    }
    return render(request, 'home/main.html', context)
