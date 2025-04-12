from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Like, Comment
from .serializers import LikeSerializer, CommentSerializer
from posts.models import Post

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Comment.objects.none()

        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(post_id=post_id)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Comment.objects.none()

        if not self.request.user.is_authenticated:
            return Comment.objects.none()

        return Comment.objects.filter(user=self.request.user)


class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            
            if created:
                serializer = LikeSerializer(like)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"detail": "You have already liked this post."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            
            try:
                like = Like.objects.get(user=request.user, post=post)
                like.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Like.DoesNotExist:
                return Response(
                    {"detail": "You have not liked this post."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post not found."},
                status=status.HTTP_404_NOT_FOUND
            )

