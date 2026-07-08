## Why

The project spec defines an Author and Post data model but neither model exists yet. Without the database schema, the blog platform has no way to store or retrieve content. This change implements the core data layer so the remaining feature work (views, URLs, search) can build on it.

## What Changes

1. **Register `blog` app** in `INSTALLED_APPS` so Django recognises the app where models will live.
2. **Create Author model** with a OneToOne link to Django's built-in `User` and a display `name` field.
3. **Create Post model** with `title`, `content`, `created_at`, and a foreign key to `Author`; default ordering by newest first.
4. **Register both models** with the Django admin site for basic CRUD visibility.
5. **Generate and run migrations** to materialise the schema in SQLite.

## Capabilities

### New Capabilities
- `author-model`: Author model — OneToOne to User, CharField for display name, `__str__()` method, registered in admin.
- `post-model`: Post model — title, content, created_at (auto), FK to Author, default ordering newest-first, `__str__()` method, registered in admin.

### Modified Capabilities

- None — no existing specs at `openspec/specs/`.

## Impact

- `blog/models.py` — new Author and Post models
- `blog/admin.py` — model admin registrations
- `TheBlogs/settings.py` — add `"blog"` to INSTALLED_APPS
- `blog/migrations/` — new migration files
- `db.sqlite3` — schema applied at migration time
