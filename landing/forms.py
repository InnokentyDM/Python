from django import forms
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}),
        }
        labels = {
            "comment": "Комментарий",
            "image": "Изображение",
        }
        exclude = [""]


