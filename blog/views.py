from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Post


def index(request):
    posts = Post.objects.select_related("author").all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related("author"), pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, "blog/author_posts.html", {"author": author, "posts": posts})


def new_post(request):
    if request.method == "POST":
        author = Author.objects.first()
        if author is None:
            return render(
                request,
                "blog/new_post.html",
                {"error": "No author available yet. An admin must create one first."},
            )
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        Post.objects.create(title=title, content=content, author=author)
        return redirect("index")
    return render(request, "blog/new_post.html")


def signup(request):
    if request.method == "POST":
        return redirect("index")
    return render(request, "blog/signup.html")
