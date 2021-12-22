from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectRegisterForm, ProjectUpdateForm

@login_required
def main(request):
    context = {
        'title': 'Home',
        'projects': Project.objects.all()
    }
    return render(request, 'home/main.html', context)


def projectRegister(request):
    if request.method == 'POST':
        project_form = ProjectRegisterForm(request.POST)
        if project_form.is_valid():

            Project.objects.create(FloatedBy = request.user)
            request.user.project.save()

            project_form = ProjectRegisterForm(request.POST, instance = request.user.project)
            project_form.save()

            project_title = project_form.cleaned_data.get('Title')
            messages.success(request, f"Project-{project_title} created!")
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        project_form = ProjectRegisterForm()

    context = {
        'title': 'New-Project',
        'project_form': project_form,
    }

    return render(request, 'home/projects.html', context)
