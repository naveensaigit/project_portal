from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

STATUS_CHOICES = (
    ('Open','Open'),
    ('Ongoing','Ongoing'),
    ('Completed','Completed')
)
DIFFICULTY_CHOICES = (
    ('Beginner','Beginner'),
    ('Intermediate','Intermediate'),
    ('Hard','Hard')
)

DURATION_CHOICES = (
    ('<1 month', '< 1 month'),
    ('1-2 months', '1-2 months'),
    ('2-4 months', '2-4 months'),
    ('4-6 months', '4-6 months'),
    ('6-12 months', '6-12 months'),
    ('>12 months', '> 12 months'),
    
)

REQUEST_STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
)

class Tag(models.Model):
    Title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Title}"

class Project(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(default = 'images.jpeg', upload_to='project_pics', blank=True, validators=[FileExtensionValidator(allowed_extensions=['png, jpg, jpeg'])])
    Description = models.TextField()
    FloatedBy = models.ForeignKey(User, on_delete=models.CASCADE,related_name="FloatedBy")
    Mentors = models.ManyToManyField(User,related_name='Mentors')
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    OpenedFor = models.CharField(max_length=300)
    Difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES, default='Beginner')
    PreRequisite = models.TextField()
    Tags = models.ManyToManyField(Tag, related_name='Tags')
    Duration = models.CharField(max_length=30, choices=DURATION_CHOICES)
    DatePosted = models.DateTimeField(default = timezone.now)
    SelectionCriteria = models.TextField()
    Question = models.TextField()
    AlreadyApplied = models.ManyToManyField(User, related_name='AlreadyApplied', blank = True)
    Likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Title}"

class ApplyRequest(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.TextField()
    Status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES)

    def __str__(self):
        return f"{self.User}->{self.Project}"
