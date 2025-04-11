from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Follow

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'bio', 'profile_picture', 
                  'date_joined', 'followers_count', 'following_count')
        read_only_fields = ('id', 'date_joined')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'profile_picture')
        read_only_fields = ('id',)

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField()
    following = serializers.StringRelatedField()
    
    class Meta:
        model = Follow
        fields = ('id', 'follower', 'following', 'created_at')
        read_only_fields = ('id', 'created_at')

