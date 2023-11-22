from rest_framework import serializers
from .models import Post

class LikeSerializer(serializers.Serializer):
    post = serializers.CharField(source='post_liked.id')
    user = serializers.CharField(source='like_author.username')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'author')
