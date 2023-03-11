from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from home.decorators import user_profile_completed, user_profile_type_set
# from .forms import UserRegisterForm, ProfileRegisterForm, ProfileUpdateForm, UserUpdateForm
from .forms import StudentProfileUpdateForm, FacultyProfileUpdateForm
from django.contrib import messages
from .models import Profile,Notification
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from functions import *
from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

class Login(LoginView):
    template_name = 'users/login.html'

# def signup(request):
#     if request.method == 'POST':
#         user_form = UserRegisterForm(request.POST)
#         profile_form = ProfileRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             newusername = user_form.cleaned_data.get('username')
#             newuser = User.objects.filter(username = newusername).first()

#             profile_form = ProfileRegisterForm(request.POST,request.FILES, instance = newuser.profile)
#             profile_form.save()

#             messages.success(request, f"Account created for {newusername}!")
#             return redirect('login')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserRegisterForm()
#         profile_form = ProfileRegisterForm()

#     context = {
#         'title': 'Register',
#         'user_form': user_form,
#         'profile_form': profile_form
#     }

#     return render(request, 'users/signup.html', context)


@login_required
@user_profile_completed
def profile(request, user_id):
    current_user = User.objects.get(id=user_id)
    projects = get_user_projects(current_user)
    projects_id = get_user_projects_id(current_user)

    var = True
    if(user_id!=request.user.id):
        var= False
        projects.pop()

    context = {
        'title': 'Profile',
        'projects': projects,
        'projects_id': projects_id,
        'notifications': Notification.objects.filter(user=request.user).order_by('-time'),
        'profile_user': current_user,
        'user_is_author' : var
    }

    return render(request, 'users/profile.html', context)

@login_required
@user_profile_type_set
def profile_edit(request):
    user_type = Profile.objects.get(user = request.user).profile_type
    if request.method == 'POST':
        # user_update_form = UserUpdateForm(request.POST, instance = request.user)
        if user_type == "Student":
            profile_update_form = StudentProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        else:
            profile_update_form = FacultyProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        # if user_update_form.is_valid() and profile_update_form.is_valid():
        if profile_update_form.is_valid():
            user_profile = Profile.objects.get(user = request.user)
            user_img = str(user_profile.image)
            user_cv = str(user_profile.cv)

            if len(request.FILES)!=0:
                if request.FILES.get('image') and user_img!="default.jpg":
                    default_storage.delete(user_img)
                elif request.FILES.get('cv') and user_cv:
                    default_storage.delete(user_cv)

            # user_update_form.save()
            profile_update_form.save()

            messages.success(request, "Your profile has been updated!")
            if request.GET.get('firstLogin') == 'True':
                return redirect('/home')
            return redirect('/profile/'+ str(request.user.id))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # user_update_form = UserUpdateForm(instance = request.user)
        if user_type == "Student":
            profile_update_form = StudentProfileUpdateForm(instance = request.user.profile)
        else:
            profile_update_form = FacultyProfileUpdateForm(instance = request.user.profile)

    context = {
        'title': 'Profile Edit',
        'notifications': Notification.objects.filter(user=request.user).order_by('-time'),
        # 'user_form': user_update_form,
        'profile_form': profile_update_form,
    }

    return render(request, 'users/profile_edit.html', context)

@login_required
@user_profile_type_set
@user_profile_completed
def projects_view(request, user_id):
    current_user = User.objects.get(id=user_id)

    req_projects, title, heading = get_projects_view_details(request, current_user)
    projects = get_filtered_projects(request, req_projects)
    projects = get_paginated_projects(request, projects)
    projects_id = get_user_projects_id(current_user)
    common_tags = get_most_common_tags(5)


    context = {
        'title': title,
        'users':User.objects.all(),
        'tags': Tag.objects.all(),
        'users_html':serialize("json", User.objects.all()),
        'tags_html':serialize("json", Tag.objects.all()),
        'projects': projects,
        'projects_id': projects_id,
        'notifications': Notification.objects.filter(user = request.user).order_by('-time'),
        'common_tags':common_tags,
        'heading': heading
    }

    return render(request, 'home/main.html', context)

def Logout(request):
    logout(request)
    return redirect('/')