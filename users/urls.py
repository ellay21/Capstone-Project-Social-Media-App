from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, LogoutView, UserProfileView,
    FollowUserView, UnfollowUserView,
    FollowersListView, FollowingListView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    path('users/<str:pk>/', UserProfileView.as_view(), name='user-profile'),
    
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('users/<int:user_id>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('users/<int:user_id>/following/', FollowingListView.as_view(), name='following-list'),
]

