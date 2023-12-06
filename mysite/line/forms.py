from django import forms
from .models import *

class AddComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-input'})
        }
        labels = {
            'text': 'Leave a comment',
        }

class AddPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-input'})
        }