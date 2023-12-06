from rest_framework import serializers
from .models import *


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'




class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'pseudo')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'author')
