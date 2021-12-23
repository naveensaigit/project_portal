from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectRegisterForm, ProjectUpdateForm
from home.decorators import user_is_project_author

@login_required
def main(request):
    context = {
        'title': 'Home',
        'projects': Project.objects.all().order_by('-DatePosted')
    }
    return render(request, 'home/main.html', context)

@login_required
def projectRegister(request):
    if request.method == 'POST':
        project_form = ProjectRegisterForm(request.POST)
        if project_form.is_valid():

            newproj = Project(FloatedBy = request.user)
            newproj.save()

            request.user.profile.projects.add(newproj)
            project_form = ProjectRegisterForm(request.POST, instance = newproj)
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

    return render(request, 'home/projectsRegister.html', context)

@login_required
def project(request, project_id):
    context = {
        'title': 'Project',
        'project': Project.objects.get(id = project_id),
    }
    return render(request, 'home/project.html', context)


@user_is_project_author
def projectUpdate(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project_update_form = ProjectUpdateForm(request.POST, instance=project)
        if project_update_form.is_valid():
            project_update_form.save()
            messages.success(request, "Project details has been updated!")
            return redirect('project', project_id = project.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        project_update_form = ProjectUpdateForm(instance=project)

    context = {
        'title': 'Update-Project',
        'project_title': project.Title,
        'project_form': project_update_form
    }

    return render(request, 'home/projectUpdate.html', context)

@user_is_project_author
def projectDelete(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project has been deleted!")
        return redirect('home')

    context = {
        'title': 'Update-Project',
        'project': project
    }

    return render(request, 'home/projectDelete.html', context)
