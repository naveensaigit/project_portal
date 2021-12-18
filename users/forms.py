from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name',
                  'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills','cv']
