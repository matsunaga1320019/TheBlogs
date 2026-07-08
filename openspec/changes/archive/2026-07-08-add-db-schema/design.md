## Context

TheBlogs is a fresh Django 5.2.15 project. The `blog` app is scaffolded (`models.py`, `admin.py`, etc.) but not registered in `INSTALLED_APPS` and has no models. The project spec defines an Author → Post data model. When models are added, Django's migration framework will produce the schema automatically. The dev database is SQLite.

## Goals / Non-Goals

**Goals:**
- Register `blog` app in `INSTALLED_APPS`
- Create `Author` model with `OneToOneField` to `auth.User` and a display `name`
- Create `Post` model with `title`, `content`, `created_at` and `ForeignKey` to `Author`
- Add `__str__()` on both models for admin readability
- Register both models in `blog/admin.py`
- Generate and apply migrations

**Non-Goals:**
- Building views, URLs, templates, or any API layer
- Adding DRF or third-party packages
- Custom user model or authentication changes
- Search, filtering, or query optimisation
- Production database setup

## Decisions

1. **App registration first, then models** — Add `"blog"` to `INSTALLED_APPS` before defining models so Django can detect migrations for the app.
2. **`OneToOneField` vs. `AbstractUser`** — Use `OneToOneField(User)` on Author rather than subclassing `AbstractUser`. This keeps Django's auth untouched, avoids migration churn on the built-in User model, and is simpler when third-party auth packages are not needed.
3. **`name` as plain `CharField`** — A single `name` field (not first/last separate) matches the project spec's simplicity goal. Max length 100 is reasonable for a display name.
4. **`created_at` with `auto_now_add=True`** — The timestamp is set once on creation and never updated. This matches the "newest first" ordering requirement and avoids accidental overwrites.
5. **Model `Meta.ordering = ["-created_at"]`** — Default ordering on the model level so all queries return newest-first without explicit `.order_by()`.
6. **Admin registration via `admin.site.register`** — Simple registration (not custom `ModelAdmin`) is sufficient for early development. Customisation can follow later.

## Risks / Trade-offs

- [Risk] Adding `OneToOneField` to User means every Author creation requires a User first → Mitigation: accept this as a design constraint; it enforces the spec's rule that only registered users can be authors.
- [Risk] Cascade delete on Author will delete all their Posts → Mitigation: `CASCADE` is the intended behaviour per spec; if soft-delete is needed later, this can be changed with a migration.
- [Risk] `name` is not unique — two authors could have the same display name → Mitigation: the underlying `User` object provides uniqueness; `name` is purely for display.
