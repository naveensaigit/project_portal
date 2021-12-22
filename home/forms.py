from django import forms
from django.contrib.auth.models import User
from .models import Project
from django.contrib.auth.forms import UserCreationForm



class ProjectRegisterForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','Difficulty','PreRequisite','Duration','SelectionCriteria','OpenedFor','AlreadyApplied']



class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','Difficulty','PreRequisite','Duration','SelectionCriteria','OpenedFor','AlreadyApplied']
