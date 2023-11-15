

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Post, Comment, Like

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'user_email', 'user_firstname', 'user_lastname', 'user_age']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)