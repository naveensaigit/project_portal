from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from users.models import Notification
from .forms import ProjectRegisterForm, ProjectUpdateForm
from home.decorators import user_is_project_author
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProjectFilter

@login_required
def main(request):
    all_project_list = Project.objects.all().order_by('-DatePosted')
    myFilter = ProjectFilter(request.GET,queryset=all_project_list)
    filtered_projects= myFilter.qs

    if request.method == "POST":
        value = request.POST['search']
        if value == "":
            searched_projects = filtered_projects
        else:
            searched_projects_Title = Project.objects.filter(Title__contains = value)
            searched_projects_Desription = Project.objects.filter(Description__contains = value)
            searched_projects = searched_projects_Title | searched_projects_Desription
            searched_projects = searched_projects.order_by('-DatePosted')
        projects = searched_projects
    else:
        projects = filtered_projects

    user_projects_id = []
    user_starred_projects_id = []
    user_requested_projects_id = []

    user_applied_projects = all_project_list.filter(AlreadyApplied =  request.user)
    user_floated_projects = all_project_list.filter(FloatedBy =  request.user)
    for project in user_applied_projects:
        user_projects_id.append(project.id)
    for project in user_floated_projects:
        user_projects_id.append(project.id)

    user_requested_projects = all_project_list.filter(ApplyRequest = request.user)
    for project in user_requested_projects:
        user_requested_projects_id.append(project.id)

    for project in request.user.profile.starred_projects.all():
        user_starred_projects_id.append(project.id)


    page = request.GET.get('page', 1)

    paginator = Paginator(projects, 5)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        'title': 'Home',
        'projects': projects,
        'user_projects_id': user_projects_id,
        'user_starred_projects_id' : user_starred_projects_id,
        'user_requested_projects_id' : user_requested_projects_id,
        'num_projects_applied' : user_applied_projects.count(),
        'num_projects_req':len(user_requested_projects_id),
        'num_projects_floated': user_floated_projects.count(),
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
        'myFilter':myFilter
    }


    return render(request, 'home/main.html', context)

@login_required
def projectRegister(request):
    if request.method == 'POST':
        project_form = ProjectRegisterForm(request.POST)
        if project_form.is_valid():

            newproj = Project(FloatedBy = request.user)
            newproj.save()

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
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
    }

    return render(request, 'home/projectsRegister.html', context)

@login_required
def project(request):
    project_id = request.GET.get('project_id')
    project = Project.objects.get(id=project_id)
    apply_requests = project.ApplyRequest.all()

    all_project_list = Project.objects.all().order_by('-DatePosted')
    user_projects_id = []
    user_starred_projects_id = []
    user_requested_projects_id = []

    user_applied_projects = all_project_list.filter(AlreadyApplied =  request.user)
    user_floated_projects = all_project_list.filter(FloatedBy =  request.user)
    for tempproject in user_applied_projects:
        user_projects_id.append(tempproject.id)
    for tempproject in user_floated_projects:
        user_projects_id.append(tempproject.id)

    user_requested_projects = all_project_list.filter(ApplyRequest = request.user)
    for tempproject in user_requested_projects:
        user_requested_projects_id.append(tempproject.id)

    for tempproject in request.user.profile.starred_projects.all():
        user_starred_projects_id.append(tempproject.id)


    context = {
        'title': 'Project',
        'project': project,
        'user_projects_id': user_projects_id,
        'user_starred_projects_id' : user_starred_projects_id,
        'user_requested_projects_id' : user_requested_projects_id,
        'apply_requests' : apply_requests,
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
    }
    return render(request, 'home/project.html', context)


@login_required
@user_is_project_author
def projectUpdate(request):
    project_id = request.GET.get('project_id')
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
        'project_form': project_update_form,
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
    }

    return render(request, 'home/projectUpdate.html', context)


@login_required
@user_is_project_author
def projectDelete(request):
    project_id = request.GET.get('project_id')
    print(project_id)
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project has been deleted!")
        return redirect('home')

    context = {
        'title': 'Update-Project',
        'project': project,
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
    }

    return render(request, 'home/projectDelete.html', context)


@login_required
def projectTask(request):
    project_id = request.GET.get('project_id')
    task = request.GET.get('task')
    page_number = request.GET.get('page_number')

    project = Project.objects.get(id=project_id)
    current_user = request.user

    if task == "Apply":
        year= current_user.profile.year
        branch=current_user.profile.branch
        if(len(year)==0 or len(branch)==0):
            messages.warning(request,"Please update your year and branch in profile section")
            return redirect('/profile/edit')
        else:
            user_branch = f"{year} Year {branch}"
            if(user_branch in project.OpenedFor):
                project.ApplyRequest.add(current_user)
                messages.success(request,"Successfully Requested!")
                notification_message=f"{current_user} has requested for {project} Project"
                project_url = f"project/{project_id}"
                notification=Notification(user=project.FloatedBy,title= "Apply Request",message=notification_message,url=project_url)
                print(notification)
                notification.save()
                # Project Mail Notification to be implemented
            else:
                messages.warning(request,"You are not eligible to opt this project.")
    if task == "Withdraw":
        project.ApplyRequest.remove(current_user)
    if task == "Leave":
        if project.FloatedBy != current_user:
            project.AlreadyApplied.remove(current_user)
            messages.success(request,f"{project} is dropped successfully.")
        else:
            messages.error(request, 'You cannot leave this project because it is floated by you.')
    if task == "Star":
        current_user.profile.starred_projects.add(project)
    if task == "Unstar":
        current_user.profile.starred_projects.remove(project)

    if page_number:
        url = f'/?page={page_number}'
    else:
        url = f'/project/?project_id={project.id}'
    return redirect(url)


def projectAccept(request):
    project_id = request.GET.get('project_id')
    request_user_name = request.GET.get('request_user_name')

    project = Project.objects.get(id=project_id)
    request_user = User.objects.filter(username = request_user_name).first()
    
    project.ApplyRequest.remove(request_user)
    project.AlreadyApplied.add(request_user)
    return redirect(f'/project/?project_id={project.id}')

def projectReject(request):
    project_id = request.GET.get('project_id')
    request_user_name = request.GET.get('request_user_name')

    project = Project.objects.get(id=project_id)
    request_user = User.objects.filter(username = request_user_name).first()

    project.ApplyRequest.remove(request_user)
    return redirect(f'/project/?project_id={project.id}')