from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

# ViewSet для User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet для Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        post.likes.add(user)
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user not in post.likes.all():
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        post.likes.remove(user)
        return Response({"detail": "Like removed successfully."}, status=status.HTTP_200_OK)

# ViewSet для Comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            return Response({"detail": "You have already liked this comment."}, status=status.HTTP_400_BAD_REQUEST)
        comment.likes.add(user)
        return Response({"detail": "Comment liked successfully."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user not in comment.likes.all():
            return Response({"detail": "You haven't liked this comment."}, status=status.HTTP_400_BAD_REQUEST)
        comment.likes.remove(user)
        return Response({"detail": "Like removed successfully."}, status=status.HTTP_200_OK)