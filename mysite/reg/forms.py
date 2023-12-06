from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from hashlib import sha256


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'user_email', 'user_firstname', 'user_lastname', 'user_age', 'pseudo')

    def clean_pseudo(self):
        if self.cleaned_data['pseudo'] == None:
            from copy import deepcopy
            name = deepcopy(self.cleaned_data['username'])
            print(name)
            self.cleaned_data['pseudo'] = sha256(str(name).encode('utf-8')).hexdigest()
            print(self.cleaned_data['pseudo'])
            return self.cleaned_data['pseudo']
        else:
            return self.cleaned_data['pseudo']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'user_email', 'user_firstname', 'user_lastname', 'user_age', 'pseudo')