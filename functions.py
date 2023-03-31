from home.models import Project, Tag, ApplyRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Notification
from django.core.mail import send_mail
from django.conf import settings
# from django.shortcuts import redirect
from django.contrib import messages
from home.filters import ProjectFilter
from django.contrib.auth.models import User
from collections import Counter
# import os
# import nltk
# nltk.download('words', download_dir=os.getcwd())
# from nltk.corpus import words

def shellScript():
    # from home.models import Project, Tag
    # projects = Project.objects.all()
    # tags = Tag.objects.all()

    # i = 7
    # for project in projects:
    #     tag = tags.get(id = i)
    #     print("Adding tag", tag, "to project", project)
    #     project.Tags.add(tag)
    #     if i==21:
    #         i = 7
    #     else:
    #         i += 1
    pass

def check_if_valid(request):
    tagname = request.GET.get('newTagTitle').upper()
    # if tagname.lower() not in words.words():
    #     message = 'Invalid word'
    #     messages.error(request, message)
    #     print("Sent message-:", message)
    #     return -1

    tag = Tag.objects.all().filter(Title = tagname)
    if len(tag)!=0:
        # message = 'Tag already exists'
        # messages.error(request, message)
        # print("Sent message-:", message)
        return 0

    return 1

def get_filtered_projects(request, all_projects):
    myFilter = ProjectFilter(request.GET,queryset=all_projects)
    filtered_projects= myFilter.qs
    return filtered_projects

def get_most_common_tags(size):
    projects = Project.objects.all()
    tags = []
    for project in projects:
        project_tags = project.Tags.all()
        for project_tag in project_tags:
            tags.append(project_tag)
    return [x for x in Counter(tags)][:size]

def get_user_projects(user):
    all_project_list = Project.objects.all().order_by('-DatePosted')
    applied = all_project_list.filter(AlreadyApplied=user)
    floated = all_project_list.filter(FloatedBy=user)

    requested = []
    for apply_request in ApplyRequest.objects.all().filter(User=user).filter(Status = "Pending"):
        requested.append(apply_request.Project)

    starred = user.profile.starred_projects.all()
    return [floated, applied, requested, starred]

def get_user_projects_id(user):
    floated_id = []
    liked_id = []
    applied_id = []
    requested_id = []
    starred_id = []

    all_project_list = Project.objects.all().order_by('-DatePosted')
    floated = all_project_list.filter(FloatedBy =  user)
    liked = user.profile.liked_projects.all()
    applied = all_project_list.filter(AlreadyApplied =  user)
    apply_requests = ApplyRequest.objects.all().filter(User=user).filter(Status = "Pending")
    starred = user.profile.starred_projects.all()

    for project in floated:
        floated_id.append(project.id)
    for project in liked:
        liked_id.append(project.id)
    for project in applied:
        applied_id.append(project.id)
    for apply_request in apply_requests:
        requested_id.append(apply_request.Project.id)
    for project in starred:
        starred_id.append(project.id)

    return [floated_id, liked_id, applied_id, requested_id, starred_id]

def get_paginated_projects(request, projects):
    page = request.GET.get('page', 1)
    number_of_projects = request.GET.get('limit')
    if(number_of_projects==None):
        number_of_projects=12

    paginator = Paginator(projects.order_by('-Likes', '-DatePosted'), number_of_projects)
    try:
        paginated_projects = paginator.page(page)
    except PageNotAnInteger:
        paginated_projects = paginator.page(1)
    except EmptyPage:
        paginated_projects = paginator.page(paginator.num_pages)
    return paginated_projects

# def apply_delimeter_seperation(projects):
#     for project in projects:
#         Flag=False
#         prereqs = str(project.PreRequisite).split('\r\n')
#         if(len(prereqs)>2):
#             Flag=True
#         prereqs= prereqs[0:2]
#         if(Flag==True):
#             prereqs.append("More Tags...")
#         project.PreRequisite = prereqs[0:3]

def get_searched_projects(request):
    value = request.POST['search']
    searched_projects_Title = Project.objects.filter(Title__contains = value)
    searched_projects_Desription = Project.objects.filter(Description__contains = value)
    searched_projects = searched_projects_Title | searched_projects_Desription
    return searched_projects

def send_mail_notification(subject, message, email_from , recipient_list):
    try:
        send_mail( subject, message, email_from, recipient_list )
    except:
        pass

def send_notification(request, project):
    project_id = request.GET.get('project_id')
    current_user = request.user

    notification_message=f"{current_user} has requested for {project} Project"
    project_url = f"/project/?project_id={project_id}"
    notification=Notification(user=project.FloatedBy, project_requested = project, notification_from = request.user, title= "Apply Request", message=notification_message,url=project_url)
    notification.save()

def delete_notification(current_user, project):
    Notification.objects.filter(notification_from = current_user).filter(project_requested = project).delete()

def apply_on_project(request, project):
    current_user = request.user
    user_branch = f"{current_user.profile.branch} {current_user.profile.year} Year"
    if("All" in project.OpenedFor or user_branch in project.OpenedFor):
        message = request.GET.get('message')
        if message == None:
            message = ""
        applyrequest = ApplyRequest(User = current_user, Project=project, Message=message, Status = "Pending")
        applyrequest.save()
        messages.success(request,"Successfully Requested!")
        send_notification(request, project)
        send_mail_notification('Project Application', f"{current_user} has requested for {project} Project", settings.EMAIL_HOST_USER, [project.FloatedBy.email,])
    else:
        messages.warning(request,"You are not eligible to opt this project.")

def withdraw_from_project(request, project):
    current_user = request.user
    delete_notification(current_user, project)
    send_mail_notification('Project Application Withdrawn', f"Your request for application on {project} Project has been withdrawn", settings.EMAIL_HOST_USER, [current_user.email,])
    send_mail_notification('Project Application Withdrawn', f"{current_user} withdrew his application for {project} Project", settings.EMAIL_HOST_USER, [project.FloatedBy.email,])
    ApplyRequest.objects.all().filter(User = current_user).filter(Project = project).delete()

def leave_project(request, project):
    current_user = request.user
    if project.FloatedBy != current_user:
        project.AlreadyApplied.remove(current_user)
        ApplyRequest.objects.all().filter(User = current_user).delete()
        delete_notification(current_user, project)
        send_mail_notification('Project Left', f"You left the {project} Project", settings.EMAIL_HOST_USER, [current_user.email,])
        send_mail_notification('Project Left', f"{current_user} left the {project} Project", settings.EMAIL_HOST_USER, [project.FloatedBy.email,])
        messages.success(request,f"{project} is dropped successfully.")
    else:
        messages.error(request, 'You cannot leave this project because it is floated by you.')

def all_apply_requests_task(project, task):
    apply_requests = ApplyRequest.objects.all().filter(Project=project)
    for apply_request in apply_requests:
        if(task=="AcceptAll"):
            apply_request_task(apply_request, "Accept")
        else:
            apply_request_task(apply_request, "Reject")

def apply_request_task(apply_request,task):
    if apply_request.Status == "Pending":
        newStatus = task + "ed"
        apply_request.Status = newStatus
        if newStatus == "Accepted":
            apply_request.Project.AlreadyApplied.add(apply_request.User)
        delete_notification(apply_request.User, apply_request.Project)
        send_mail_notification(f'Project Application {newStatus}', f"Your application for {apply_request.Project} Project has been {newStatus}", settings.EMAIL_HOST_USER, [apply_request.User.email,])
        apply_request.save()

def do_task(request):
    project_id = request.GET.get('project_id')
    task = request.GET.get('task')

    project = Project.objects.get(id=project_id)
    current_user = request.user

    if task == "Leave":
        leave_project(request, project)
    elif task == "Star":
        current_user.profile.starred_projects.add(project)
    elif task == "Unstar":
        current_user.profile.starred_projects.remove(project)
    elif task == "Like":
        if project not in current_user.profile.liked_projects.all():
            current_user.profile.liked_projects.add(project)
            project.Likes += 1
            project.save()
    elif task == "Unlike":
        if project in current_user.profile.liked_projects.all():
            current_user.profile.liked_projects.remove(project)
            project.Likes -= 1
            project.save()
    elif task == "Apply":
        apply_on_project(request, project)
    elif task == "Withdraw":
        withdraw_from_project(request,project)
    elif task == "Accept" or task == "Reject":
        request_user_name = request.GET.get('request_user')
        request_user = User.objects.filter(username = request_user_name).first()
        apply_request = ApplyRequest.objects.all().filter(User = request_user).filter(Project = project).first()

        apply_request_task(apply_request, task)
    elif task == "AcceptAll" or task == "RejectAll":
        all_apply_requests_task(project, task)

def get_projects_view_details(request, current_user):
    view = request.GET.get('view')
    all_projects = Project.objects.all()
    if view == "applied":
        req_projects = all_projects.filter(AlreadyApplied = current_user)
        title = 'Projects Applied'
        heading = "Projects Applied For:"
    elif view == "requested":
        req_projects_id = list(ApplyRequest.objects.all().filter(User = current_user).values_list('Project', flat=True))
        req_projects = Project.objects.all().filter(id__in = req_projects_id)
        title = 'Projects Requested'
        heading = "Projects Requested:"
    elif view == "floated":
        req_projects = all_projects.filter(FloatedBy = current_user)
        title = 'Projects Floated'
        heading = "Projects Floated:"
    else:
        req_projects = current_user.profile.starred_projects.all()
        title = 'Projects Starred'
        heading = "Projects Starred:"
    req_projects = req_projects.order_by('-DatePosted')
    return req_projects, title, heading

def check_user_profile(user):
    # user_fields = [user.username, user.first_name, user.last_name, user.email]
    user_fields = [user.username, user.first_name, user.email]
    for field in user_fields:
        if field == None or (len(field) == 0):
            print(" user fields is not completed")
            return True

    profile = user.profile
    general_profile = [profile.image, str(profile.cv)]
    for field in general_profile:
        if field == None or (len(field) == 0):
            print(" General profile is not completed")
            return True

    person = profile.profile_type
    if person == "Student":
        student_profile = [profile.techskills.all(), profile.rollno ,profile.year ,profile.branch]
        for field in student_profile:
            if field == None or (len(field) == 0):
                print(" Student profile is not completed")
                return True
    else:
        faculty_profile = [profile.area_of_interest, profile.school]
        for field in faculty_profile:
            if field == None or (len(field) == 0):
                print(" Faculty profile is not completed")
                return True
    return False
    # if str(profile.cv) == "" or len(profile.techskills.all()) == 0:
    #     return True
    # return False