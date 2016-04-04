import datetime
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    link = models.CharField(max_length=50)
    date_pablished = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField()