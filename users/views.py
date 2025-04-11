from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Follow
from .serializers import UserSerializer, UserProfileSerializer, FollowSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user
        return super().get_object()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            
            if request.user == user_to_follow:
                return Response(
                    {"detail": "You cannot follow yourself."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
                return Response(
                    {"detail": "You are already following this user."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            follow = Follow.objects.create(follower=request.user, following=user_to_follow)
            serializer = FollowSerializer(follow)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            
            try:
                follow = Follow.objects.get(follower=request.user, following=user_to_unfollow)
                follow.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Follow.DoesNotExist:
                return Response(
                    {"detail": "You are not following this user."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()

        user_id = self.kwargs.get('user_id')
        return User.objects.filter(following__following_id=user_id)


class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()

        user_id = self.kwargs.get('user_id')
        return User.objects.filter(followers__follower_id=user_id)


