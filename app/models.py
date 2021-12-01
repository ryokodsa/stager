from django.db import models
from django.conf import settings
from django.utils import timezone

class Calendar(models.Model):
    title = models.CharField('タイトル', max_length=100)
    link = models.CharField('リンク', max_length=1000)


    def __str__(self):
        return self.title
"""
class Choice(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
"""

#ここから新しいやつ
class troupes(models.Model):
    troupe = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.troupe