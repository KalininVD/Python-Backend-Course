from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404
from .models import User, Post, Comment
from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer, PostSerializer, CommentSerializer, CreateCommentSerializer, UpdateCommentSerializer

# View for CRUD operations on User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

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

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]

        return [IsAuthenticated()]

# View for CRUD operations on Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated()]

        return [AllowAny()]

# View for CRUD operations on Comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateCommentSerializer
        elif self.action in ["update", "partial_update"]:
            return UpdateCommentSerializer

        return CommentSerializer

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAuthenticated()]

        return [AllowAny()]


# View for likes on Post
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

# View for likes on Comment
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


# View for User's posts and comments
class UserPostsView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Post.objects.filter(author_id=user_id).order_by("-created_at")

# View for sorting User's posts by likes
class UserPostsSortByLikesView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return (
            Post.objects.filter(author_id=user_id)
            .annotate(likes_count=Count("likes"))
            .order_by("-likes_count")
        )

# View for sorting User's posts by updated time
class UserPostsSortByUpdatedTimeView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Post.objects.filter(author_id=user_id).order_by("-updated_at")


# View for User's comments
class UserCommentsView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Comment.objects.filter(author_id=user_id).order_by("-created_at")

# View for sorting User's comments by likes
class UserCommentsSortByLikesView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return (
            Comment.objects.filter(author_id=user_id)
            .annotate(likes_count=Count("likes"))
            .order_by("-likes_count")
        )

# View for sorting User's comments by updated time
class UserCommentsSortByUpdatedTimeView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Comment.objects.filter(author_id=user_id).order_by("-updated_at")


# View for comments on a post
class PostCommentsView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post_id=post_id).order_by("created_at")

# View for sorting comments on a post by likes
class PostCommentsSortByLikesView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return (
            Comment.objects.filter(post_id=post_id)
            .annotate(likes_count=Count("likes"))
            .order_by("-likes_count")
        )

# View for sorting comments on a post by updated time
class PostCommentsSortByUpdatedTimeView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post_id=post_id).order_by("-updated_at")


# View for User's stats
class UserStatsView(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        # Подсчёт поставленных лайков
        likes_given_posts = Post.objects.filter(likes=user).count()
        likes_given_comments = Comment.objects.filter(likes=user).count()

        # Подсчёт полученных лайков
        likes_received_posts = (
            Post.objects.filter(author=user)
            .annotate(likes_count=Count("likes"))
            .aggregate(Sum("likes_count"))["likes_count__sum"]
            or 0
        )
        likes_received_comments = (
            Comment.objects.filter(author=user)
            .annotate(likes_count=Count("likes"))
            .aggregate(Sum("likes_count"))["likes_count__sum"]
            or 0
        )

        # Подсчёт опубликованных постов и комментариев
        total_posts = Post.objects.filter(author=user).count()
        total_comments = Comment.objects.filter(author=user).count()

        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "likes_given": likes_given_posts + likes_given_comments,
                "likes_given_on_posts": likes_given_posts,
                "likes_given_on_comments": likes_given_comments,
                "likes_received": likes_received_posts + likes_received_comments,
                "likes_received_on_posts": likes_received_posts,
                "likes_received_on_comments": likes_received_comments,
                "total_posts": total_posts,
                "total_comments": total_comments,
            }
        )


# View for top 5 posts by likes
class TopPostsView(APIView):
    def get(self, request):
        top_posts = Post.objects.annotate(likes_count=Count("likes")).order_by("-likes_count")[:5]
        serializer = PostSerializer(top_posts, many=True)
        return Response(serializer.data)

# View for top 5 posts by number of comments
class MostCommentedPostsView(APIView):
    def get(self, request):
        top_posts = (
            Post.objects
            .annotate(comments_count=Count("comments", distinct=True))
            .order_by("-comments_count")[:5]
        )
        serializer = PostSerializer(top_posts, many=True)
        return Response(serializer.data)

# View for top 5 comments by likes
class TopCommentsView(APIView):
    def get(self, request):
        top_comments = Comment.objects.annotate(likes_count=Count("likes")).order_by("-likes_count")[:5]
        serializer = CommentSerializer(top_comments, many=True)
        return Response(serializer.data)