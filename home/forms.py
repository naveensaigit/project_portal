from django import forms
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms.formsets import all_valid
from .models import Project
from users.models import User

OPENED_FOR_CHOICES = (
    ('All','All'),
    ('CSE',(
        ('CSE 1st Year', 'CSE 1st Year'),
        ('CSE 2nd Year', 'CSE 2nd Year'),
        ('CSE 3rd Year', 'CSE 3rd Year'),
        ('CSE 4th Year', 'CSE 4th Year'),
        )
    ),
    ('DSE',(
        ('DSE 1st Year', 'DSE 1st Year'),
        ('DSE 2nd Year', 'DSE 2nd Year'),
        ('DSE 3rd Year', 'DSE 3rd Year'),
        ('DSE 4th Year', 'DSE 4th Year'),
        )
    ),
    ('CE',(
        ('CE 1st Year', 'CE 1st Year'),
        ('CE 2nd Year', 'CE 2nd Year'),
        ('CE 3rd Year', 'CE 3rd Year'),
        ('CE 4th Year', 'CE 4th Year'),
        )
    ),
    ('BioE',(
        ('BioE 1st Year', 'BioE 1st Year'),
        ('BioE 2nd Year', 'BioE 2nd Year'),
        ('BioE 3rd Year', 'BioE 3rd Year'),
        ('BioE 4th Year', 'BioE 4th Year'),
        )
    ),
)

class ProjectRegisterForm(forms.ModelForm):
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=OPENED_FOR_CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria','MailNotification']



class ProjectUpdateForm(forms.ModelForm):
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=OPENED_FOR_CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria','MailNotification']
