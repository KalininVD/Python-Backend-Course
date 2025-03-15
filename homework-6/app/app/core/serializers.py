from rest_framework import serializers
from .models import User, Post, Comment

# Сериализатор для User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Сериализатор для Post
class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

# Сериализатор для Comment
class CommentSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'