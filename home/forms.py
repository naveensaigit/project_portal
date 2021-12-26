from django import forms
from .models import Project



class ProjectRegisterForm(forms.ModelForm):
    CHOICES = (
        ('0','None'),
        ('1', '1st Year CSE'),
        ('2', '1st Year DSE'),
        ('3', '1st Year EE'),
        ('4', '1st Year ME'),
        ('5', '1st Year CE'),
        ('6', '1st Year BioE'),
        ('7', '2nd Year CSE'),
        ('8', '2nd Year DSE'),
        ('9', '2nd Year EE'),
        ('10', '2nd Year ME'),
        ('11', '2nd Year CE'),
        ('12', '2nd Year BioE'),
        ('13', '3rd Year CSE'),
        ('14', '3rd Year DSE'),
        ('15', '3rd Year EE'),
        ('16', '3rd Year ME'),
        ('17', '3rd Year CE'),
        ('18', '3rd Year BioE'),
        ('19', '4th Year CSE'),
        ('20', '4th Year DSE'),
        ('21', '4th Year EE'),
        ('22', '4th Year ME'),
        ('23', '4th Year CE'),
        ('24', '4th Year BioE'),
    )
    OpenedFor = forms.MultipleChoiceField(
        label="Opened For", choices=CHOICES, required=True)
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria']



class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Title','Description','Mentors','Status','OpenedFor','Difficulty','PreRequisite','Duration','SelectionCriteria']
