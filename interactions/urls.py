from django.urls import path
from .views import (
    CommentListCreateView, CommentDetailView,
    LikeView, UnlikeView
)

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='like-post'),
    path('posts/<int:post_id>/unlike/', UnlikeView.as_view(), name='unlike-post'),
]

