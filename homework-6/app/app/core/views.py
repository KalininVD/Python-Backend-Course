from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        if user in post.likes.all():
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.add(user)
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        if user not in post.likes.all():
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.remove(user)
        return Response({"detail": "Like removed successfully."}, status=status.HTTP_200_OK)


class LikeCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        user = request.user

        if user in comment.likes.all():
            return Response({"detail": "You already liked this comment."}, status=status.HTTP_400_BAD_REQUEST)

        comment.likes.add(user)
        return Response({"detail": "Comment liked successfully."}, status=status.HTTP_200_OK)

    def delete(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        user = request.user

        if user not in comment.likes.all():
            return Response({"detail": "You haven't liked this comment."}, status=status.HTTP_400_BAD_REQUEST)

        comment.likes.remove(user)
        return Response({"detail": "Like removed successfully."}, status=status.HTTP_200_OK)