from django import forms
from .models import Project
from django_select2 import forms as s2forms

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

class MentorsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "username__icontains",
    ]
class TagsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "Title__icontains",
    ]

class ProjectRegisterForm(forms.ModelForm):
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=OPENED_FOR_CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Tags','Duration','SelectionCriteria','MailNotification']
        widgets = {
            "Mentors": MentorsWidget,
            "Tags": TagsWidget,
        }


class ProjectUpdateForm(forms.ModelForm):
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=OPENED_FOR_CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Tags','Duration','SelectionCriteria','MailNotification']
        widgets = {
            "Mentors": MentorsWidget,
            "Tags": TagsWidget,
        }
