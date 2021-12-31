from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import FileInput
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(
        widget = FileInput(),
    )
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv']