from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, ProfileRegisterForm, UserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage

def signup(request):
    # request.POST is actually a dictionary containing all the form fields as key and there form values as values for respective keys
    # request.user -> person creating request i.e. person logged in django-admin
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            newusername = user_form.cleaned_data.get('username')
            newuser = User.objects.filter(username = newusername).first()

            profile_form = ProfileRegisterForm(request.POST,request.FILES, instance = newuser.profile)
            # instance tells to which profile should we save the data
            # we could manually also save the data
            # newuserprofile = Profile(user = newuser, rollno = request.Post.rollno ............)
            # newuserprofile.save()
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
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance = request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            print(request.user.profile.image)
            user = request.user
            user_img = User.objects.filter(username = user).first().profile.image
            image_to_be_deleted = str(user_img)
            if(len(request.FILES)!=0 and image_to_be_deleted!="default.jpg"):
                default_storage.delete(image_to_be_deleted)
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
        'title': 'Profile',
        'user_form': user_update_form,
        'profile_form': profile_update_form
    }

    return render(request, 'users/profile.html', context)

# Database queries
    # Profile.objects.all() -> it gives queryset
    # Profile.objects.all().first() -> first element of queryset
    # Profile.objects.filter(<anyfilter like username = 'rajat'>)
    # tempvar = Profile(user = User.objects.all().first(),rollno = 'B20123'...)
    # tempvar.rollno -> accessing fields
    # tempvar.save()