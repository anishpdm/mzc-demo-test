from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweets(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date=models.DateTimeField(default=timezone.now)


# Create your models here.
