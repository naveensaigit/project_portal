from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, ProfileRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from home.models import Project

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
def profile(request):
    context = {
        'title': 'Profile',
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
    projects = Project.objects.all()
    projects_floated = projects.filter(FloatedBy = request.user)
    
    context = {
        'title': 'Projects Floated',
        'projects': projects_floated,
    }

    return render(request, 'users/profile_floated.html', context)

def projects_applied(request):
    projects = Project.objects.all()
    projects_applied = projects.filter(AlreadyApplied = request.user)
    
    context = {
        'title': 'Projects Applied',
        'projects' : projects_applied,
    }

    return render(request, 'users/profile_applied.html', context)
    pass

def projects_starred(request):
    projects_starred = request.user.profile.starred_projects.all()
    
    context = {
        'title': 'Projects Starred',
        'projects' : projects_starred,
    }

    return render(request, 'users/profile_starred.html', context)
    pass

def projects_requested(request):
    projects = Project.objects.all()
    projects_requested = projects.filter(ApplyRequest = request.user)
    context = {
        'title': 'Projects Requested',
        'projects': projects_requested,
    }
    return render(request, 'users/profile_requested.html', context)
