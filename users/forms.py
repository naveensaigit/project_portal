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
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv','linked_in_link','portfolio_link','github_link']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []


class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(
        widget = FileInput(),
        required=False
    )
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv','linked_in_link','portfolio_link','github_link']