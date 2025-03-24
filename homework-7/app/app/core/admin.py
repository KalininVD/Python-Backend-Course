from django.contrib import admin
from .models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "date_joined", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "updated_at")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at", "updated_at", "author")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "created_at", "updated_at")
    search_fields = ("content", "author__username", "post__title")
    list_filter = ("created_at", "updated_at", "author", "post")