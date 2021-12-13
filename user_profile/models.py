from django.db import models

# YEAR_CHOICES = [
#     ('1st', '1st'),
#     ('2nd', '2nd'),
#     ('3rd', '3rd'),
#     ('4th', '4th'),
# ]

# class profile(models.Model):
#     name = models.CharField(max_length=100)
#     rollno = models.CharField(max_length=6)
#     branch = models.TextField()
#     year = models.CharField(choices=YEAR_CHOICES, default='1st')

#     def __str__(self):
#         return self.name+"("+self.rollno+")"

# class skills(models.Model):
#     rollno = models.ForeignKey(profile.rollno, on_delete=models.CASCADE)
