from django.urls import path
from .views import LikeView, UnlikeView
from . import views
from django.conf import settings
from django.http import HttpRequest

urlpatterns = [
    path('', views.show),
    path('<str:post_id>/', views.show_post),

    path('api/post/<str:id>/like/', LikeView.as_view()),
    path('api/post/<str:id>/unlike/', UnlikeView.as_view()),
    #path('like_unlike/', views.like_unlike_post, name='like_unlike_post'),
]

