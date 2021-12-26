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
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
    )
    BRANCH_CHOICES = (
        ('1', 'CSE'),
        ('2', 'DSE'),
        ('3', 'ME'),
        ('4', 'EE'),
        ('5', 'CE'),
        ('6', 'BioE'),
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
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
    )
    BRANCH_CHOICES = (
        ('1', 'CSE'),
        ('2', 'DSE'),
        ('3', 'ME'),
        ('4', 'EE'),
        ('5', 'CE'),
        ('6', 'BioE'),
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
