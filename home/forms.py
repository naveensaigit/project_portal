from django import forms
from .models import Project
from django.forms.widgets import FileInput

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
    ('EE',(
        ('EE 1st Year', 'EE 1st Year'),
        ('EE 2nd Year', 'EE 2nd Year'),
        ('EE 3rd Year', 'EE 3rd Year'),
        ('EE 4th Year', 'EE 4th Year'),
        )
    ),
    ('ME',(
        ('ME 1st Year', 'ME 1st Year'),
        ('ME 2nd Year', 'ME 2nd Year'),
        ('ME 3rd Year', 'ME 3rd Year'),
        ('ME 4th Year', 'ME 4th Year'),
        )
    ),
    ('EP',(
        ('EP 1st Year', 'EP 1st Year'),
        ('EP 2nd Year', 'EP 2nd Year'),
        ('EP 3rd Year', 'EP 3rd Year'),
        ('EP 4th Year', 'EP 4th Year'),
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
    Image = forms.FileField(
        widget = FileInput(),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super(ProjectRegisterForm, self).__init__(*args, **kwargs)
        self.fields['Question'].label = "What question would you like to ask to the applicant?"
    class Meta:
        model = Project
        fields = ['Title', 'Image', 'Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Tags','Duration','SelectionCriteria', 'Question']



class ProjectUpdateForm(forms.ModelForm):
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=OPENED_FOR_CHOICES, required=True,
        widget = forms.CheckboxSelectMultiple(),    
    )
    Image = forms.FileField(
        widget = FileInput(),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        self.fields['Question'].label = "What question would you like to ask to the applicant?"
    class Meta:
        model = Project
        fields = ['Title', 'Image', 'Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Tags','Duration','SelectionCriteria', 'Question']
