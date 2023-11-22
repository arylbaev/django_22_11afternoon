from django.urls import path
from .views import LikeView, UnlikeView, PostAPIView
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.show),
    #path('f/', views.show)
    path('<str:post_id>/<str:user_id>/', views.show_post),
    #path('<str:post_id>/None/', views.show_post),
    #path('<str:post_id>/f/', views.show_post_guest),
    path('<str:post_id>/<str:user_id>/like/', views.like_post),

    #path('api/post/<int:id>/like/', LikeView.as_view(), name='like'),
    #path('api/post/<int:id>/unlike/', UnlikeView.as_view(), name='unlike'),
    #path('api/postlist', PostAPIView.as_view()),
    #path('like_unlike/', views.like_unlike_post, name='like_unlike_post'),
]

