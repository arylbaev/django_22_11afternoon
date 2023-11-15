from django.db import models
from django.urls import reverse
# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    username = models.CharField(max_length=25, unique=True)
    user_firstname = models.CharField(max_length=25)
    user_lastname = models.CharField(max_length=25)
    user_age = models.IntegerField(default=0)
    user_email = models.EmailField(unique=True)
    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Like(models.Model):
    post_liked = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post_liked", "like_author")

    def __str__(self):
        return f''
