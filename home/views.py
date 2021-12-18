from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/main.html', context)
