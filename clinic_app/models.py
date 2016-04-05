import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    link = models.CharField(max_length=50)
    date_published = models.DateTimeField(default=timezone.now())
    image = models.ImageField()

    def __unicode__(self):
        return self.title
