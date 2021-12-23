from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectRegisterForm, ProjectUpdateForm
from home.decorators import user_is_project_author
from home.models import Project

@login_required
def main(request):
    user_projects_id = []
    user_starred_projects_id = []
    for project in request.user.profile.projects.all():
        user_projects_id.append(project.id)

    for project in request.user.profile.starred_projects.all():
        user_starred_projects_id.append(project.id)
    context = {
        'title': 'Home',
        'projects': Project.objects.all().order_by('-DatePosted'),
        'user_projects_id': user_projects_id,
        'user_starred_projects_id' : user_starred_projects_id
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


@login_required
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


@login_required
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


@login_required
def projectApply(request, project_id):
    project = Project.objects.get(id=project_id)
    current_user = request.user

    project.AlreadyApplied.add(current_user)
    current_user.profile.projects.add(project)
    messages.success(request,"Successfully Apllied!")
    return redirect('home')


@login_required
def projectLeave(request, project_id):
    project = Project.objects.get(id=project_id)
    current_user = request.user
    
    if project.FloatedBy != current_user:
        project.AlreadyApplied.remove(current_user)
        current_user.profile.projects.remove(project)
        messages.success(request,f"{project} is dropped successfully.")
    else:
        messages.error(request, 'You cannot leave this project because it is floated by you.')
    return redirect('home')

def projectStar(request, project_id):
    project = Project.objects.get(id=project_id)
    current_user = request.user

    current_user.profile.starred_projects.add(project)
    return redirect('home')

def projectUnStar(request, project_id):
    project = Project.objects.get(id=project_id)
    current_user = request.user

    current_user.profile.starred_projects.remove(project)
    return redirect('home')
