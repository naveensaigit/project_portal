from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('1','Open'),
    ('2','Ongoing'),
    ('3','Completed')
)
DIFFICULTY_CHOICES = (
    ('1','Beginner'),
    ('2','Intermediate'),
    ('3','Hard')
)

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    FloatedBy = models.CharField(max_length=30)
    Mentors = models.TextField()
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Open')
    Difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='Beginner')
    PreRequisite = models.TextField()
    Duration = models.DurationField()
    DatePosted = models.DateTimeField(default = timezone.now)
    SelectionCriteria = models.TextField()
    OpenedFor = models.TextField()
    AlreadyApplied = models.TextField()

    def __str__(self):
        return f"{self.Title}({self.DatePosted})"