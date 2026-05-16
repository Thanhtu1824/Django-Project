from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Client (models.Model):

    GENDER_CHOICES = [
        ('Nam','True'),
        ('Nu','False'),
    ]

    name = models.CharField(max_length = 100)
    gender = models.CharField(choices = GENDER_CHOICES, default = True)
    active = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Post (models.Model):

    author = models.ForeignKey(Client, on_delete = models.CASCADE, related_name = 'all_post')
    title = models.CharField(max_length=100)
    content = models.CharField()
    created_post = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author.name} - {self.title}'