from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileRegisterForm(forms.ModelForm):
    YEAR_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
    )
    BRANCH_CHOICES = (
        ('CSE', 'CSE'),
        ('DSE', 'DSE'),
        ('ME', 'ME'),
        ('EE', 'EE'),
        ('CE', 'CE'),
        ('BioE', 'BioE'),
    )
    year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=True,
        widget=forms.Select(attrs={'yr': 'form-control input-sm'})
    )
    branch = forms.ChoiceField(
        label="Branch", choices=BRANCH_CHOICES, required=True,
        widget=forms.Select(attrs={'yr': 'form-control input-sm'})
    )
    
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    YEAR_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
    )
    BRANCH_CHOICES = (
        ('CSE', 'CSE'),
        ('DSE', 'DSE'),
        ('ME', 'ME'),
        ('EE', 'EE'),
        ('CE', 'CE'),
        ('BioE', 'BioE'),
    )
    year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=True,
        widget=forms.Select(attrs={'yr': 'form-control input-sm'})
    )
    branch = forms.ChoiceField(
        label="Branch", choices=BRANCH_CHOICES, required=True,
        widget=forms.Select(attrs={'yr': 'form-control input-sm'})
    )
    class Meta:
        model = Profile
        fields = ['image', 'rollno', 'year', 'branch', 'techskills', 'cv']
