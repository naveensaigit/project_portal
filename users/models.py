from django.db import models
from django.contrib.auth.models import User


YEAR_CHOICES = (
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
    ('5', '5th'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    rollno = models.CharField(max_length=10)
    year = models.CharField(max_length=10,choices=YEAR_CHOICES, default='1st')
    branch = models.CharField(max_length=30)
    techskills = models.TextField()
    cv = models.FileField(blank = True, upload_to='resumes')

    def __str__(self):
        return f"{self.user}({self.rollno})"
