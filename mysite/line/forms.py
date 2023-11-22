from django import forms
from models import Comment


class AddCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    #author =