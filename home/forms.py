from django import forms
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms.formsets import all_valid
from .models import Project
from users.models import User



class ProjectRegisterForm(forms.ModelForm):
    CHOICES = (
        ('0','None'),
        ('1st Year CSE', '1st Year CSE'),
        ('1st Year DSE', '1st Year DSE'),
        ('1st Year ME', '1st Year ME'),
        ('1st Year CE', '1st Year CE'),
        ('1st Year BioE', '1st Year BioE'),
        ('2nd Year CSE', '2nd Year CSE'),
        ('2nd Year DSE', '2nd Year DSE'),
        ('2nd Year ME', '2nd Year ME'),
        ('2nd Year CE', '2nd Year CE'),
        ('2nd Year BioE', '2nd Year BioE'),
        ('3rd Year CSE', '3rd Year CSE'),
        ('3rd Year DSE', '3rd Year DSE'),
        ('3rd Year ME', '3rd Year ME'),
        ('3rd Year CE', '3rd Year CE'),
        ('3rd Year BioE', '3rd Year BioE'),
        ('4th Year CSE', '4th Year CSE'),
        ('4th Year DSE', '4th Year DSE'),
        ('4th Year ME', '4th Year ME'),
        ('4th Year CE', '4th Year CE'),
        ('4th Year BioE', '4th Year BioE'),
    )
    NOTIFICATION_CHOICES = (
        ('ON','ON'),
        ('OFF','OFF'),
    )
    
    # Mentors = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.all(),
    #     widget = forms.CheckboxSelectMultiple(),
    # )
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria','MailNotification']



class ProjectUpdateForm(forms.ModelForm):
    CHOICES = (
        ('0','None'),
        ('1st Year CSE', '1st Year CSE'),
        ('1st Year DSE', '1st Year DSE'),
        ('1st Year ME', '1st Year ME'),
        ('1st Year CE', '1st Year CE'),
        ('1st Year BioE', '1st Year BioE'),
        ('2nd Year CSE', '2nd Year CSE'),
        ('2nd Year DSE', '2nd Year DSE'),
        ('2nd Year ME', '2nd Year ME'),
        ('2nd Year CE', '2nd Year CE'),
        ('2nd Year BioE', '2nd Year BioE'),
        ('3rd Year CSE', '3rd Year CSE'),
        ('3rd Year DSE', '3rd Year DSE'),
        ('3rd Year ME', '3rd Year ME'),
        ('3rd Year CE', '3rd Year CE'),
        ('3rd Year BioE', '3rd Year BioE'),
        ('4th Year CSE', '4th Year CSE'),
        ('4th Year DSE', '4th Year DSE'),
        ('4th Year ME', '4th Year ME'),
        ('4th Year CE', '4th Year CE'),
        ('4th Year BioE', '4th Year BioE'),
    )
    NOTIFICATION_CHOICES = (
        ('ON','ON'),
        ('OFF','OFF'),
    )
    # Mentors = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.all(),
    #     widget = forms.CheckboxSelectMultiple(),
    # )
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria','MailNotification']
