from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, ProfileRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from home.models import Project
from home.filters import ProjectFilter

def signup(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            newusername = user_form.cleaned_data.get('username')
            newuser = User.objects.filter(username = newusername).first()

            profile_form = ProfileRegisterForm(request.POST,request.FILES, instance = newuser.profile)
            profile_form.save()

            messages.success(request, f"Account created for {newusername}!")
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()

    context = {
        'title': 'Register',
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/signup.html', context)


@login_required
def profile(request, user_id):
    all_project_list = Project.objects.all().order_by('-DatePosted')

    user_projects_id = []
    user_starred_projects_id = []
    user_requested_projects_id = []

    user_applied_projects = all_project_list.filter(AlreadyApplied=request.user)
    user_floated_projects = all_project_list.filter(FloatedBy=request.user)
    for project in user_applied_projects:
        user_projects_id.append(project.id)
    for project in user_floated_projects:
        user_projects_id.append(project.id)

    user_requested_projects = all_project_list.filter(ApplyRequest=request.user)
    for project in user_requested_projects:
        user_requested_projects_id.append(project.id)

    for project in request.user.profile.starred_projects.all():
        user_starred_projects_id.append(project.id)

    context = {
        'title': 'Profile',
        'num_projects_applied': user_applied_projects.count(),
        'num_projects_req': len(user_requested_projects_id),
        'num_projects_floated': user_floated_projects.count(),
        'user_starred_projects_id' : user_starred_projects_id,
        'profile_user': User.objects.get(id = user_id)
    }

    return render(request, 'users/profile.html', context)

def profile_edit(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance = request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_profile = Profile.objects.get(user = request.user)
            user_img = str(user_profile.image)
            user_cv = str(user_profile.cv)

            if len(request.FILES)!=0:
                if request.FILES.get('image') and user_img!="default.jpg":
                    default_storage.delete(user_img)
                elif request.FILES.get('cv') and user_cv:
                    default_storage.delete(user_cv)

            user_update_form.save()
            profile_update_form.save()

            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_update_form = UserUpdateForm(instance = request.user)
        profile_update_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'title': 'Profile Edit',
        'user_form': user_update_form,
        'profile_form': profile_update_form,
    }

    return render(request, 'users/profile_edit.html', context)

def projects_floated(request):
    all_project_list = Project.objects.all().filter(FloatedBy = request.user).order_by('-DatePosted')
    myFilter = ProjectFilter(request.GET,queryset=all_project_list)
    filtered_projects= myFilter.qs
    user_starred_projects_id = []
    for project in (filtered_projects and request.user.profile.starred_projects.all()):
        user_starred_projects_id.append(project.id)
    context = {
        'title': 'Projects Floated',
        'projects': filtered_projects,
        'myFilter': myFilter,
        'user_starred_projects_id' : user_starred_projects_id,
    }

    return render(request, 'users/profile_floated.html', context)

def projects_applied(request):
    all_project_list = Project.objects.all().filter(AlreadyApplied = request.user).order_by('-DatePosted')
    myFilter = ProjectFilter(request.GET,queryset=all_project_list)
    filtered_projects= myFilter.qs
    
    context = {
        'title': 'Projects Applied',
        'projects' : filtered_projects,
        'myFilter': myFilter,
    }

    return render(request, 'users/profile_applied.html', context)

def projects_starred(request):
    projects_starred = request.user.profile.starred_projects.all()
    myFilter = ProjectFilter(request.GET, queryset=projects_starred)
    filtered_projects = myFilter.qs
    user_starred_projects_id = []
    for project in request.user.profile.starred_projects.all():
        user_starred_projects_id.append(project.id)
    context = {
        'title': 'Projects Starred',
        'projects' : filtered_projects,
        'user_starred_projects_id' : user_starred_projects_id,
        'myFilter': myFilter,
    }

    return render(request, 'users/profile_starred.html', context)

def projects_requested(request):
    all_project_list = Project.objects.all().filter(ApplyRequest = request.user).order_by('-DatePosted')
    myFilter = ProjectFilter(request.GET,queryset=all_project_list)
    filtered_projects= myFilter.qs
    user_starred_projects_id = []
    for project in (filtered_projects and request.user.profile.starred_projects.all()):
        user_starred_projects_id.append(project.id)

    context = {
        'title': 'Projects Requested',
        'projects': filtered_projects,
        'myFilter': myFilter,
        'user_starred_projects_id' : user_starred_projects_id,
    }
    return render(request, 'users/profile_requested.html', context)

def oauth(request):
    url = '/accounts/google/login/?process=login/'
    return redirect(url)