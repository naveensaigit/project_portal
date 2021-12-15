from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserForm, ProfileForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile

def main(req):
    return HttpResponse('Hi , On profile page')


def register(request):
    # request.POST is actually a dictionary containing all the form fields as key and there form values as values for respective keys
    # request.user -> person creating request i.e. person logged in django-admin
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            newusername = user_form.cleaned_data.get('username')
            newuser = User.objects.filter(username = newusername).first()

            profile_form = ProfileForm(request.POST, instance = newuser.profile)
            # instance tells to which profile should we save the data
            # we could manually also save the data
            # newuserprofile = Profile(user = newuser, rollno = request.Post.rollno ............)
            # newuserprofile.save()
            profile_form.save()

            messages.success(request, f"Account created for {newusername}!")
            return redirect('project_portal-home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/register.html', context)

# Database queries
    # Profile.objects.all() -> it gives queryset
    # Profile.objects.all().first() -> first element of queryset
    # Profile.objects.filter(<anyfilter like username = 'rajat'>)
    # tempvar = Profile(user = User.objects.all().first(),rollno = 'B20123'...)
    # tempvar.rollno -> accessing fields
    # tempvar.save()