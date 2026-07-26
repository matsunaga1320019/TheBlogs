## Why

The blog application has models and admin configured but no public-facing views. Users cannot browse, create, or filter blog posts without HTML views that render the content.

## What Changes

- Add a home page view listing all posts with title, author, and date
- Add a post detail view showing full content
- Add an author-filtered post list view at `/author/<author_id>/`
- Add a new post creation form at `/new/` (GET shows form, POST creates and redirects)
- Add a stub signup page at `/signup/` (GET shows form, POST redirects to index)
- Create base and page templates with minimal HTML structure
- Wire up URL routes for all new views

## Capabilities

### New Capabilities

- `post-list`: View displaying a chronological list of blog posts with title, author name, and creation date
- `post-detail`: View displaying a single post's full content, author, and timestamp
- `author-posts`: View at `/author/<author_id>/` displaying only posts by a specific author, returning 404 if author not found
- `new-post`: Form view at `/new/` for creating a new Post (GET renders form, POST creates with暂定 author and redirects to index)
- `signup`: Stub form view at `/signup/` (GET renders form, POST redirects to index without creating User/Author)

### Modified Capabilities

(none)

## Impact

- `blog/views.py`: New view functions for all five views
- `blog/urls.py`: New file with URL patterns (included from project urls)
- `blog/templates/`: New template directory with HTML files (base, post_list, post_detail, author_posts, new_post, signup)
- `TheBlogs/urls.py`: Add include for blog app URLs