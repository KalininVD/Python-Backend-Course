from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import User, Post, Comment
from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer, PostSerializer, CommentSerializer

# ViewSet для User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        elif self.action in ["update", "partial_update"]:
            return UpdateUserSerializer

        return UserSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return User.objects.all()

        return User.objects.filter(id=user.id)

    @swagger_auto_schema(request_body=CreateUserSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=UpdateUserSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


# ViewSet для Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ViewSet для Comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer