from django.db import models
from django.conf import settings
from django.utils import timezone

class Calendar(models.Model):
    title = models.CharField('タイトル', max_length=100)

    def __str__(self):
        return self.title

