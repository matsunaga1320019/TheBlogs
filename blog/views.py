from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, SignupForm
from .models import Author, Post


def index(request):
    posts = Post.objects.select_related("author").all()
    return render(request, "blog/post_list.html", {"posts": posts})


def search_posts(request):
    query = request.GET.get("q", "").strip()
    posts = Post.objects.select_related("author").all()
    if query:
        posts = posts.filter(title__icontains=query)
    return render(request, "blog/_post_results.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related("author"), pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, "blog/author_posts.html", {"author": author, "posts": posts})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.author
            post.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "blog/new_post.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(user=user, name=user.username)
            login(request, user)
            return redirect("index")
    else:
        form = SignupForm()
    return render(request, "blog/signup.html", {"form": form})
