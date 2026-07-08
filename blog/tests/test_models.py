from datetime import datetime, timezone

import pytest
from django.contrib.auth import get_user_model

from blog.models import Author, Post

User = get_user_model()


@pytest.mark.django_db
class TestAuthorModel:
    def test_str_returns_name(self):
        user = User.objects.create_user(username="jdoe")
        author = Author.objects.create(user=user, name="Jane Doe")
        assert str(author) == "Jane Doe"


@pytest.mark.django_db
class TestPostModel:
    def test_str_returns_title(self):
        user = User.objects.create_user(username="jdoe")
        author = Author.objects.create(user=user, name="Jane Doe")
        post = Post.objects.create(
            title="My Post", content="Hello", author=author
        )
        assert str(post) == "My Post"

    def test_default_ordering_newest_first(self):
        user = User.objects.create_user(username="jdoe")
        author = Author.objects.create(user=user, name="Jane Doe")
        older = Post.objects.create(title="Older", content="A", author=author)
        newer = Post.objects.create(title="Newer", content="B", author=author)
        Post.objects.filter(pk=older.pk).update(
            created_at=datetime(2025, 1, 1, tzinfo=timezone.utc)
        )
        Post.objects.filter(pk=newer.pk).update(
            created_at=datetime(2026, 1, 1, tzinfo=timezone.utc)
        )
        posts = list(Post.objects.all())
        assert posts == [newer, older]

    def test_delete_author_cascades_to_posts(self):
        user = User.objects.create_user(username="jdoe")
        author = Author.objects.create(user=user, name="Jane Doe")
        Post.objects.create(title="P1", content="A", author=author)
        Post.objects.create(title="P2", content="B", author=author)
        assert Post.objects.count() == 2
        author.delete()
        assert Post.objects.count() == 0
