from datetime import datetime, timezone

import pytest
from django.contrib.auth import get_user_model

from blog.models import Author, Post

User = get_user_model()


@pytest.mark.django_db
class TestIndexView:
    def test_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_shows_all_posts_ordered_newest_first(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        p1 = Post.objects.create(title="First", content="A", author=author)
        p2 = Post.objects.create(title="Second", content="B", author=author)
        Post.objects.filter(pk=p1.pk).update(
            created_at=datetime(2025, 1, 1, tzinfo=timezone.utc)
        )
        Post.objects.filter(pk=p2.pk).update(
            created_at=datetime(2026, 1, 1, tzinfo=timezone.utc)
        )
        response = client.get("/")
        posts = list(response.context["posts"])
        assert posts == [p2, p1]

    def test_empty_list(self, client):
        response = client.get("/")
        posts = list(response.context["posts"])
        assert posts == []


@pytest.mark.django_db
class TestPostDetailView:
    def test_returns_200(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        post = Post.objects.create(title="Hello", content="Body", author=author)
        response = client.get(f"/post/{post.pk}/")
        assert response.status_code == 200

    def test_returns_404_for_missing_post(self, client):
        response = client.get("/post/99999/")
        assert response.status_code == 404


@pytest.mark.django_db
class TestAuthorPostsView:
    def test_returns_200(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        Post.objects.create(title="P1", content="A", author=author)
        response = client.get(f"/author/{author.pk}/")
        assert response.status_code == 200

    def test_returns_404_for_missing_author(self, client):
        response = client.get("/author/99999/")
        assert response.status_code == 404

    def test_filters_posts_by_author(self, client):
        u1 = User.objects.create_user(username="u1")
        u2 = User.objects.create_user(username="u2")
        alice = Author.objects.create(user=u1, name="Alice")
        bob = Author.objects.create(user=u2, name="Bob")
        p1 = Post.objects.create(title="A1", content="x", author=alice)
        p2 = Post.objects.create(title="A2", content="y", author=alice)
        Post.objects.create(title="B1", content="z", author=bob)
        response = client.get(f"/author/{alice.pk}/")
        posts = list(response.context["posts"])
        assert len(posts) == 2
        assert p1 in posts
        assert p2 in posts

    def test_orders_newest_first(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        p1 = Post.objects.create(title="Old", content="A", author=author)
        p2 = Post.objects.create(title="New", content="B", author=author)
        Post.objects.filter(pk=p1.pk).update(
            created_at=datetime(2025, 1, 1, tzinfo=timezone.utc)
        )
        Post.objects.filter(pk=p2.pk).update(
            created_at=datetime(2026, 1, 1, tzinfo=timezone.utc)
        )
        response = client.get(f"/author/{author.pk}/")
        posts = list(response.context["posts"])
        assert posts == [p2, p1]


@pytest.mark.django_db
class TestNewPostView:
    def test_get_redirects_to_login_when_anonymous(self, client):
        response = client.get("/new/")
        assert response.status_code == 302
        assert response.url.startswith("/login/")

    def test_get_returns_200_when_logged_in(self, client):
        user = User.objects.create_user(username="u1", password="pw12345")
        Author.objects.create(user=user, name="Alice")
        client.login(username="u1", password="pw12345")
        response = client.get("/new/")
        assert response.status_code == 200

    def test_post_creates_post_and_redirects(self, client):
        user = User.objects.create_user(username="u1", password="pw12345")
        Author.objects.create(user=user, name="Alice")
        client.login(username="u1", password="pw12345")
        assert Post.objects.count() == 0
        response = client.post("/new/", {"title": "T", "content": "C"})
        assert response.status_code == 302
        assert response.url == "/"
        assert Post.objects.count() == 1
        post = Post.objects.first()
        assert post.title == "T"
        assert post.content == "C"
        assert post.author.name == "Alice"

    def test_post_with_blank_title_returns_200_and_no_post(self, client):
        user = User.objects.create_user(username="u1", password="pw12345")
        Author.objects.create(user=user, name="Alice")
        client.login(username="u1", password="pw12345")
        response = client.post("/new/", {"title": "", "content": "C"})
        assert response.status_code == 200
        assert Post.objects.count() == 0

    def test_post_without_login_redirects_and_no_post(self, client):
        response = client.post("/new/", {"title": "T", "content": "C"})
        assert response.status_code == 302
        assert response.url.startswith("/login/")
        assert Post.objects.count() == 0


@pytest.mark.django_db
class TestSearchPostsView:
    def test_returns_200(self, client):
        response = client.get("/search/")
        assert response.status_code == 200

    def test_no_query_returns_all_posts(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        Post.objects.create(title="Alpha", content="x", author=author)
        Post.objects.create(title="Beta", content="y", author=author)
        response = client.get("/search/")
        assert list(response.context["posts"]).__len__() == 2

    def test_filters_by_title_case_insensitive(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        match = Post.objects.create(title="Django Tips", content="x", author=author)
        Post.objects.create(title="Cooking", content="y", author=author)
        response = client.get("/search/", {"q": "django"})
        posts = list(response.context["posts"])
        assert posts == [match]

    def test_no_match_returns_empty(self, client):
        user = User.objects.create_user(username="u1")
        author = Author.objects.create(user=user, name="Alice")
        Post.objects.create(title="Alpha", content="x", author=author)
        response = client.get("/search/", {"q": "zzz-no-match"})
        assert list(response.context["posts"]) == []
        assert b"No posts found." in response.content

    def test_uses_partial_template_without_full_page_chrome(self, client):
        response = client.get("/search/")
        assert b"<html" not in response.content
    def test_get_returns_200(self, client):
        response = client.get("/signup/")
        assert response.status_code == 200

    def test_post_creates_user_author_and_redirects(self, client):
        assert User.objects.count() == 0
        assert Author.objects.count() == 0
        response = client.post(
            "/signup/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "a-strong-pw-93",
                "password2": "a-strong-pw-93",
            },
        )
        assert response.status_code == 302
        assert response.url == "/"
        assert User.objects.count() == 1
        assert Author.objects.count() == 1
        assert Author.objects.first().name == "newuser"

    def test_post_with_mismatched_passwords_creates_nothing(self, client):
        response = client.post(
            "/signup/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "a-strong-pw-93",
                "password2": "different",
            },
        )
        assert response.status_code == 200
        assert User.objects.count() == 0
        assert Author.objects.count() == 0
