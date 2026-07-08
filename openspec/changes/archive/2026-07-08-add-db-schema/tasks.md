## 1. App Registration

- [x] 1.1 Add `"blog"` to `INSTALLED_APPS` in `TheBlogs/settings.py`
- [x] 1.2 Run `uv run python manage.py check` to confirm app loads correctly

## 2. Author Model

- [x] 2.1 Define `Author` model in `blog/models.py` with `user` (OneToOneField to `auth.User`, CASCADE) and `name` (CharField max_length=100)
- [x] 2.2 Add `__str__()` method returning `self.name`
- [x] 2.3 Register `Author` in `blog/admin.py` with `admin.site.register()`

## 3. Post Model

- [x] 3.1 Define `Post` model in `blog/models.py` with `title` (CharField max_length=200), `content` (TextField), `created_at` (DateTimeField auto_now_add=True), and `author` (ForeignKey to `Author`, CASCADE)
- [x] 3.2 Add `Meta.ordering = ["-created_at"]` for default newest-first ordering
- [x] 3.3 Add `__str__()` method returning `self.title`
- [x] 3.4 Register `Post` in `blog/admin.py` with `admin.site.register()`

## 4. Migrations & Verification

- [x] 4.1 Run `uv run python manage.py makemigrations blog` to generate migration files
- [x] 4.2 Run `uv run python manage.py migrate` to apply the schema to SQLite
- [x] 4.3 Run `uv run pytest` to confirm existing tests still pass
