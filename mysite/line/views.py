from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie


from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *


def show(request):
    posts = Post.objects.all()
    return render(request, 'line.html', {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'line/post.html', {'post': post})


class LikeView(CreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):

        serializer_class = LikeSerializer()
        post = serializer_class.post
        user = serializer_class.user
        like = Like.create(post=post, user=user)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class UnlikeView(DestroyAPIView):

    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(id=kwargs["id"])
        like = Like.objects.get(user=user, post=post)
        like.delete()

        return Response(status=status.HTTP_200_OK)









