from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from home.decorators import user_profile_completed
from .forms import UserRegisterForm, ProfileRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Profile,Notification
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from functions import *
from django.core.serializers import serialize
from django.contrib.auth import logout

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
            if request.GET.get('firstLogin') == 'True':
                return redirect('/')
            return redirect('/profile/'+ str(request.user.id))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_update_form = UserUpdateForm(instance = request.user)
        profile_update_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'title': 'Profile Edit',
        'user_form': user_update_form,
        'notifications': Notification.objects.filter(user=request.user).order_by('-time'),
        'profile_form': profile_update_form,
    }

    return render(request, 'users/profile_edit.html', context)

@login_required
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

    return render(request, 'users/projects_view.html', context)

def oauth(request):
    url = '/accounts/google/login/?process=login/'
    return redirect(url)

def Logout(request):
    logout(request)
    return redirect('/login')