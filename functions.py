from home.models import Project, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Notification
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from home.filters import ProjectFilter
from django.contrib.auth.models import User

def get_filtered_projects(request):
    all_projects = Project.objects.all().order_by('-DatePosted')
    myFilter = ProjectFilter(request.GET,queryset=all_projects)
    filtered_projects= myFilter.qs
    return filtered_projects

def get_tagged_projects(request):
    all_projects = Project.objects.all().order_by('-DatePosted')
    tagTitle = request.GET.get('tag')
    tag = Tag.objects.all().filter(Title = tagTitle)
    return all_projects.filter(Tags__in = tag)


def get_projects_id(request):
    user_floated_projects_id = []
    user_liked_projects_id = []
    user_applied_projects_id = []
    user_requested_projects_id = []
    user_starred_projects_id = []

    all_project_list = Project.objects.all().order_by('-DatePosted')
    user_floated_projects = all_project_list.filter(FloatedBy =  request.user)
    user_liked_projects = request.user.profile.liked_projects.all()
    user_applied_projects = all_project_list.filter(AlreadyApplied =  request.user)
    user_requested_projects = all_project_list.filter(ApplyRequest = request.user)
    user_starred_projects = request.user.profile.starred_projects.all()

    for project in user_floated_projects:
        user_floated_projects_id.append(project.id)
    for project in user_liked_projects:
        user_liked_projects_id.append(project.id)
    for project in user_applied_projects:
        user_applied_projects_id.append(project.id)
    for project in user_requested_projects:
        user_requested_projects_id.append(project.id)
    for project in user_starred_projects:
        user_starred_projects_id.append(project.id)

    return [user_floated_projects_id, user_liked_projects_id, user_applied_projects_id, user_requested_projects_id, user_starred_projects_id]

def get_paginated_projects(request, projects):
    page = request.GET.get('page', 1)
    paginator = Paginator(projects, 6)
    try:
        paginated_projects = paginator.page(page)
    except PageNotAnInteger:
        paginated_projects = paginator.page(1)
    except EmptyPage:
        paginated_projects = paginator.page(paginator.num_pages)
    return paginated_projects

def apply_delimeter_seperation(projects):
    for project in projects:
        Flag=False
        prereqs = str(project.PreRequisite).split('\r\n')
        if(len(prereqs)>2):
            Flag=True
        prereqs= prereqs[0:2]
        if(Flag==True):
            prereqs.append("More Tags...")
        project.PreRequisite = prereqs[0:3]

def get_searched_projects(request):
    value = request.POST['search']
    searched_projects_Title = Project.objects.filter(Title__contains = value)
    searched_projects_Desription = Project.objects.filter(Description__contains = value)
    searched_projects = searched_projects_Title | searched_projects_Desription
    searched_projects = searched_projects.order_by('-DatePosted')
    return searched_projects

def send_notification(request, project):
    project_id = request.GET.get('project_id')
    current_user = request.user

    notification_message=f"{current_user} has requested for {project} Project"
    project_url = f"/project/?project_id={project_id}"
    notification=Notification(user=project.FloatedBy, project_requested = project, notification_from = request.user, title= "Apply Request", message=notification_message,url=project_url)
    notification.save()

    if project.MailNotification == "On":
        subject = 'Project Application'
        message = notification_message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [project.FloatedBy.email,]
        send_mail( subject, message, email_from, recipient_list )

def delete_notification(request, project):
    Notification.objects.filter(notification_from = request.user).filter(project_requested = project).delete()

def apply_on_project(request, project):
    current_user = request.user
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
            send_notification(request, project)
        else:
            messages.warning(request,"You are not eligible to opt this project.")

def withdraw_from_project(request, project):
    current_user = request.user
    delete_notification(request, project)
    project.ApplyRequest.remove(current_user)

def leave_project(request, project):
    current_user = request.user
    if project.FloatedBy != current_user:
        project.AlreadyApplied.remove(current_user)
        messages.success(request,f"{project} is dropped successfully.")
    else:
        messages.error(request, 'You cannot leave this project because it is floated by you.')

def do_task(request, task):
    project_id = request.GET.get('project_id')

    project = Project.objects.get(id=project_id)
    current_user = request.user

    if task == "Apply":
        apply_on_project(request, project)
    elif task == "Withdraw":
        withdraw_from_project(request,project)
    elif task == "Leave":
        leave_project(request, project)
    elif task == "Star":
        current_user.profile.starred_projects.add(project)
    elif task == "Unstar":
        current_user.profile.starred_projects.remove(project)
    elif task == "Like":
        current_user.profile.liked_projects.add(project)
        project.Likes += 1
        project.save()
    elif task == "Unlike":
        current_user.profile.liked_projects.remove(project)
        project.Likes -= 1
        project.save()
    elif task == "Accept" or task == "Reject":
        request_user_name = request.GET.get('request_user')
        request_user = User.objects.filter(username = request_user_name).first()

        project.ApplyRequest.remove(request_user)
        if task == "Apply":
            project.AlreadyApplied.add(request_user)
