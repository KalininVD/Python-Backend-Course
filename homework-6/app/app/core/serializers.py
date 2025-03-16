from django.utils import timezone
from rest_framework import serializers
from .models import User, Post, Comment


# User model serializers (for CRUD operations)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", )

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    is_superuser = serializers.BooleanField(required=False, default=False)
    is_staff = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "is_superuser", "is_staff", )
        ref_name = None

    def validate(self, attrs):
        request = self.context.get("request")
        user = request.user if request else None

        if not (user and user.is_authenticated and user.is_superuser):
            if attrs.get("is_superuser", False) or attrs.get("is_staff", False):
                raise serializers.ValidationError(
                    "You do not have permission to set admin fields."
                )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        user = request.user if request else None

        if not (user and user.is_authenticated and user.is_superuser):
            data.pop("is_superuser", None)
            data.pop("is_staff", None)

        return data


class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", )
        ref_name = None

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password:
            instance.set_password(password)

        return super().update(instance, validated_data)


# Post model serializer (for CRUD operations)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author", "title", "content", "created_at", "updated_at", "likes", )
        read_only_fields = ("author", "created_at", "updated_at", "likes", )

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        validated_data["created_at"] = validated_data["updated_at"] = timezone.now()
        validated_data["likes"] = []
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_at"] = timezone.now()
        return super().update(instance, validated_data)


# Comment model serializers (for CRUD operations)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "author", "content", "created_at", "updated_at", "likes", )

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("author", "post", "content", "created_at", "updated_at", )
        read_only_fields = ("author", "created_at", "updated_at", )
        ref_name = None

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user

        now_time = timezone.now()
        validated_data["created_at"] = validated_data["updated_at"] = now_time

        return super().create(validated_data)

class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("author", "post", "content", "likes", "created_at", "updated_at", )
        read_only_fields = ("author", "post", "created_at", "updated_at", "likes", )
        ref_name = None

    def update(self, instance, validated_data):
        validated_data["updated_at"] = timezone.now()
        return super().update(instance, validated_data)