## 1. URL Configuration

- [x] 1.1 Create `blog/urls.py` with empty `urlpatterns` list
- [x] 1.2 Add `include('blog.urls')` to `TheBlogs/urls.py` urlpatterns

## 2. Templates

- [x] 2.1 Create `blog/templates/blog/base.html` with HTML skeleton and `{% block content %}`
- [x] 2.2 Create `blog/templates/blog/post_list.html` extending base with post listing markup
- [x] 2.3 Create `blog/templates/blog/post_detail.html` extending base with single post markup
- [x] 2.4 Create `blog/templates/blog/author_posts.html` extending base with author-filtered post listing
- [x] 2.5 Create `blog/templates/blog/new_post.html` extending base with post creation form
- [x] 2.6 Create `blog/templates/blog/signup.html` extending base with stub signup form

## 3. Views

- [x] 3.1 Add `index` function view to `blog/views.py`: query Post objects ordered by `-created_at`, render `post_list.html`
- [x] 3.2 Add `post_detail` function view: get Post by pk (404 if missing), render `post_detail.html`
- [x] 3.3 Add `author_posts` function view: get Author by pk (404 if missing), filter posts by that author, render `author_posts.html`
- [x] 3.4 Add `new_post` function view: GET renders form, POST validates and creates Post with `author=Author.objects.first()`, redirect to index
- [x] 3.5 Add `signup` function view: GET renders form, POST redirects to index without creating objects
- [x] 3.6 Wire all five URL patterns in `blog/urls.py`: `path('', index)`, `path('post/<int:pk>/', post_detail)`, `path('author/<int:author_id>/', author_posts)`, `path('new/', new_post)`, `path('signup/', signup)`

## 4. Verification

- [x] 4.1 Run `uv run pytest` and confirm all tests pass
- [x] 4.2 Run `uv run pylint blog TheBlogs` and fix any errors