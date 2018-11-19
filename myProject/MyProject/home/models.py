from django.db import models
from django.utils import timezone

# Create your models here.

class Faculties(models.Model):
    FacultyName=models.CharField(max_length=150)
    Designation=models.CharField(max_length=150)
    EmailId=models.CharField(max_length=150)
    Mobile=models.CharField(max_length=150)
    Date_Entry=models.DateTimeField(default=timezone.now)
    

