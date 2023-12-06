from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from .models import *
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view, renderer_classes

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from django.views.generic import View

from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .forms import *
import json
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

def show(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'line.html', {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    form = AddComment
    if user.is_authenticated:
        return render(request, 'line/post.html', {'post': post, 'user': user, 'form': form})
    else:
        return render(request, 'line/post.html', {'post': post})


def make_post_template(request):
    user = request.user
    form = AddPost
    if user.is_authenticated:
        return render(request, 'line/create_post.html', {'user': user, 'form': form})


def show_profile(request, user_slug):
    user = get_object_or_404(CustomUser, pseudo=user_slug)
    posts = Post.objects.filter(author=user.pk)
    """datas = []
    for p in posts:
        data = dict(title=p.title, description=p.description, photo=p.photo,
                    date_posted=p.date_posted, author=p.author)
        datas.append(data)"""
    print(posts)
    return render(request, 'line/profile.html', {'user': user, 'posts': posts})


class LikeDetail(APIView): #create like
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        post = get_object_or_404(Post, pk=data['post_id'])
        user = get_object_or_404(CustomUser, pk=data['user_id'])
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            l, created = Like.objects.get_or_create(post_liked=post, like_author=user)
            if not created:
                l.delete()

        return Response(status=status.HTTP_200_OK)


class CommentDetail(APIView): #create comment
    def post(self, request, *args, **kwargs):
        data = request.data
        post = get_object_or_404(Post, pk=data['post_id'])
        user = get_object_or_404(CustomUser, pk=data['user_id'])
        text = data['comment']
        print(post, user, text)
        Comment.objects.create(post=post, author=user, text=text)

        return Response(status=status.HTTP_200_OK)


class PostDetail(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        post = data['post']
        user = data['user_id']
        description = data['text']
