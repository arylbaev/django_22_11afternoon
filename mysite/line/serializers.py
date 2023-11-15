from rest_framework import serializers


class LikeSerializer(serializers.Serializer):

    required = False

    post = serializers.CharField(source='post_liked.id')
    user = serializers.CharField(source='like_author.username')