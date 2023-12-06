from django.db import models
from django.db.models.signals import *
from django.urls import reverse
# Create your models here.
from django.core.signals import request_finished
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashlib import sha256


class CustomUser(AbstractUser):

    def gethash(self):
        from copy import deepcopy
        name = deepcopy(self.username)
        print(name)
        pseudo = sha256(str(name).encode('utf-8')).hexdigest()
        print(pseudo)
        return pseudo

    # add additional fields in here
    username = models.CharField(max_length=64, unique=True)
    user_firstname = models.CharField(max_length=25)
    user_lastname = models.CharField(max_length=25)
    user_age = models.IntegerField(default=0)
    user_email = models.EmailField(unique=True)
    pseudo = models.SlugField(max_length=64, unique=True, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

"""
@receiver(pre_init, sender=CustomUser)
def create_pseudo(sender, **kwargs):
    try:
        if kwargs['pseudo'] is None:
            from copy import deepcopy
            name = deepcopy(kwargs['username'])
            print(name)
            kwargs['pseudo'] = sha256(str(name).encode('utf-8')).hexdigest()
    except:
        pass"""


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.author}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=700)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}, {self.post}, {self.text}'


class Like(models.Model):
    post_liked = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='likes')
    like_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    #timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post_liked", "like_author")

    def __str__(self):
        return f'{self.post_liked}, {self.like_author}'


class Follower(models.Model):
    who = models.ForeignKey(CustomUser, related_name='who', on_delete=models.CASCADE, null=True)
    whom = models.ForeignKey(CustomUser, related_name='whom', on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ("who", "whom")

    def __str__(self):
        return f''