from django import forms
from . import models

class Wallpapercreate(forms.ModelForm):
    class Meta:
        model = models.Wallpaper
        fields = ['title','body','wallpaper']





