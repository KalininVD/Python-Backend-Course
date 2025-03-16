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
    likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False,
    )

    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'likes', 'created_at', 'updated_at', )

    def create(self, validated_data):
        validated_data.pop('likes', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('likes', None)
        return super().update(instance, validated_data)

# Comment model serializer (for CRUD operations)
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=True,
    )

    likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False,
    )

    class Meta:
        model = Comment
        fields = ('author', 'post', 'content', 'likes', 'created_at', 'updated_at', )

    def create(self, validated_data):
        validated_data.pop('likes', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('likes', None)
        return super().update(instance, validated_data)