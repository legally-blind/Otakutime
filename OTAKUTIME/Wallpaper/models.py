from django.db import models
from django import forms
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Wallpaper(models.Model):
    title = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from = 'title')
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    wallpaper = models.ImageField(upload_to='wallpapers/')

    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[0:30] + ' ...'
