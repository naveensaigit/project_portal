from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    FloatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Mentors = models.ManyToManyField(User, related_name='Mentors')
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    Difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES, default='Beginner')
    PreRequisite = models.TextField()
    Duration = models.CharField(max_length=30)
    DatePosted = models.DateTimeField(default = timezone.now)
    SelectionCriteria = models.TextField()
    OpenedFor = models.TextField()
    AlreadyApplied = models.ManyToManyField(User, related_name='AlreadyApplied')

    def __str__(self):
        print(self.Title)
        return f"({self.Title} -> {self.DatePosted.date()})"