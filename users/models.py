from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from home.models import Project
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from home.models import Tag

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics', blank=True, validators=[FileExtensionValidator(allowed_extensions=['png, jpg, jpeg'])])
    rollno = models.CharField(max_length=10)
    year = models.CharField(max_length=30, choices = YEAR_CHOICES)
    branch = models.CharField(max_length=30, choices = BRANCH_CHOICES)
    techskills = models.ManyToManyField(Tag, related_name='techskills')
    starred_projects = models.ManyToManyField(Project, related_name='starred_projects', blank = True)
    liked_projects = models.ManyToManyField(Project, related_name='liked_projects', blank = True)
    cv = models.FileField(upload_to='resumes',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    linked_in_link = models.CharField(blank=True, max_length=100)
    portfolio_link = models.CharField(blank=True, max_length=100)
    github_link = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.user}({self.rollno})"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            dimensions = (300, 300)
            img.thumbnail(dimensions)
            img.save(self.image.path)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
    project_requested = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_requested")
    notification_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_creater")
    title = models.CharField(max_length=30)
    message = models.TextField()
    time = models.DateTimeField(default = timezone.now)
    url=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.title}({self.message})"