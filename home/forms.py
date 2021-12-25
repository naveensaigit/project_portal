from django import forms
from .models import Project



class ProjectRegisterForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','Difficulty','PreRequisite','Duration','SelectionCriteria','OpenedFor']



class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','Difficulty','PreRequisite','Duration','SelectionCriteria','OpenedFor']
