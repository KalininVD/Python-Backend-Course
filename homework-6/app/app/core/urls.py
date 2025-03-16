from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet, LikePostView, LikeCommentView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like_post'),
    path('comments/<int:comment_id>/like/', LikeCommentView.as_view(), name='like_comment'),
]