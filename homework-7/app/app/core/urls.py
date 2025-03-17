from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PostViewSet, CommentViewSet,
    LikePostView, LikeCommentView,
    UserPostsView, UserPostsSortByLikesView, UserPostsSortByUpdatedTimeView,
    UserCommentsView, UserCommentsSortByLikesView, UserCommentsSortByUpdatedTimeView,
    PostCommentsView, PostCommentsSortByLikesView, PostCommentsSortByUpdatedTimeView,

    UserStatsView, TopPostsView, MostCommentedPostsView, TopCommentsView,
)

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like_post"),
    path("comments/<int:comment_id>/like/", LikeCommentView.as_view(), name="like_comment"),

    path("users/<int:user_id>/posts/", UserPostsView.as_view(), name="user-posts"),
    path("users/<int:user_id>/posts/sort_by_likes/", UserPostsSortByLikesView.as_view(), name="user-posts-likes"),
    path("users/<int:user_id>/posts/sort_by_time/", UserPostsSortByUpdatedTimeView.as_view(), name="user-posts-time"),

    path("users/<int:user_id>/comments/", UserCommentsView.as_view(), name="user-comments"),
    path("users/<int:user_id>/comments/sort_by_likes/", UserCommentsSortByLikesView.as_view(), name="user-comments-likes"),
    path("users/<int:user_id>/comments/sort_by_time/", UserCommentsSortByUpdatedTimeView.as_view(), name="user-comments-time"),

    path("posts/<int:post_id>/comments/", PostCommentsView.as_view(), name="post-comments"),
    path("posts/<int:post_id>/comments/sort_by_likes/", PostCommentsSortByLikesView.as_view(), name="post-comments-likes"),
    path("posts/<int:post_id>/comments/sort_by_time/", PostCommentsSortByUpdatedTimeView.as_view(), name="post-comments-time"),

    path("users/<int:user_id>/stats/", UserStatsView.as_view(), name="user-stats"),
    path("posts/most_liked/", TopPostsView.as_view(), name="top-posts"),
    path("posts/most_commented/", MostCommentedPostsView.as_view(), name="most-commented-posts"),
    path("comments/most_liked/", TopCommentsView.as_view(), name="top-comments"),
]