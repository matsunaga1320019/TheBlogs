from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("author/<int:author_id>/", views.author_posts, name="author_posts"),
    path("new/", views.new_post, name="new_post"),
    path("signup/", views.signup, name="signup"),
]
