from rest_framework import serializers
from .models import Like, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_picture')

class CommentSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class LikeSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')

