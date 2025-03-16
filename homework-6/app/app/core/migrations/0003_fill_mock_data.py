from django.db import migrations


def fill_mock_data(apps, schema_editor):
    User = apps.get_model("core", "User")
    Post = apps.get_model("core", "Post")
    Comment = apps.get_model("core", "Comment")

    admin = User.objects.create_user(username="admin", password="sZ@b+pd5$-)UAh(cE#4xPv", is_superuser=True, is_staff=True)
    staff = User.objects.create_user(username="staff", password="mWDGahU8V2Cn-d5%,TS:J$", is_staff=True)
    superuser = User.objects.create_user(username="superuser", password="XHtb-(%`w=2F^>s3@8{UyA", is_superuser=True)
    user = User.objects.create_user(username="user", password="password")

    post_1 = Post.objects.create(author=admin, title="First post", content="Hello, world!")
    post_2 = Post.objects.create(author=user, title="New post", content="Lorem ipsum dolor sit amet, consectetuer adipiscing elit.")

    comment_1 = Comment.objects.create(author=staff, post=post_1, content="Nice post!")
    comment_2 = Comment.objects.create(author=admin, post=post_2, content="Foo...")

    post_1.likes.add(superuser)
    post_2.likes.add(superuser, user)

    comment_1.likes.add(admin)
    comment_2.likes.add(admin, staff)


def delete_mock_data(apps, schema_editor):
    User = apps.get_model("core", "User")
    Post = apps.get_model("core", "Post")
    Comment = apps.get_model("core", "Comment")

    Comment.objects.all().delete()
    Post.objects.all().delete()
    User.objects.filter(username__in=["admin", "staff", "superuser", "user"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment_updated_at_comment_likes_post_likes'),
    ]

    operations = [
        migrations.RunPython(fill_mock_data, delete_mock_data),
    ]