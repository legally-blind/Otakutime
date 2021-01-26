from django import forms
from . import models

class Videocreate(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = ['title','body','video']