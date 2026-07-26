## Context

TheBlogs is a Django 5.2 blog application with Author and Post models already defined and registered in admin. The `blog` app is already in `INSTALLED_APPS`, has no URL configuration, and no public-facing views. The project uses Python 3.11, pytest-django for testing, and black/pylint for formatting and linting.

## Goals / Non-Goals

**Goals:**
- Render a home page listing all posts (newest first) with title, author, and date
- Render a post detail page showing full content, author, and timestamp
- Render an author-filtered post list at `/author/<author_id>/` with 404 for unknown authors
- Provide a new post creation form at `/new/` (暂定 author from `Author.objects.first()`)
- Provide a stub signup page at `/signup/` that redirects without creating objects
- Use plain function-based views (`def view(request): ...`)
- Keep templates minimal with a shared base layout

**Non-Goals:**
- Authentication, login, or real author assignment
- Pagination (can be added later)
- CSS frameworks or styling beyond basic structure
- API endpoints or JSON responses
- Post editing or deletion

## Decisions

**Use function-based views (FBVs) instead of class-based views.**
Plain `def` views are explicit, easy to read, and have no framework overhead. Each view handles its own queryset, context, and response directly. Alternatives: CBVs (ListView/DetailView) hide logic behind mixins; DRF (API-focused, wrong tool here).

**Create a `blog/urls.py` included from the project root.**
Keeps URL routing modular. The blog app owns its URL namespace. Alternatives: all URLs in `TheBlogs/urls.py` (doesn't scale) or app-level namespace (unnecessary for a single app).

**Place templates in `blog/templates/blog/` following Django's app-level template convention.**
Allows `APP_DIRS` loading (default). Namespacing under `blog/` avoids collisions if other apps are added.

**Use a single `base.html` with block overrides.**
Minimal overhead. All page templates extend `base.html` and override the `content` block.

**New post view uses暂定 author assignment.**
Since authentication is not yet implemented, `new_post` assigns `author=Author.objects.first()`. This will be replaced when auth is added.

**Signup is a stub.**
`signup` renders a form and redirects on POST without creating User or Author objects. Real implementation deferred to a future auth change.

## Risks / Trade-offs

- **No pagination on list views** → Large post counts will render slowly. Mitigation: explicitly out of scope; can be added trivially later.
- **Minimal styling** → Pages will look unstyled. Mitigation: acceptable for initial delivery; CSS is a separate change.
- **Signup is non-functional** → Users may expect it to work. Mitigation: clearly a stub; will be implemented with auth.