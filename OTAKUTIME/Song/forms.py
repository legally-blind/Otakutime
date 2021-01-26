from django import forms
from . import models

class Songcreate(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ['title','body','song','image']