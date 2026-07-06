# TheBlogs — AGENTS.md

## Quick start

```powershell
# dev server
uv run manage.py runserver
# tests
uv run pytest
# lint
uv run pylint blog TheBlogs
# format
uv run black .
# coverage
uv run coverage run -m pytest
uv run coverage report
uv run coverage html
```

## Toolchain

| Tool         | Config / notes                                            |
|--------------|-----------------------------------------------------------|
| **uv**       | Package manager (`uv.lock`). Install: `uv sync`           |
| **Python**   | 3.11 (`.python-version`)                                  |
| **Django**   | 5.2.15. Settings module: `TheBlogs.settings`              |
| **pytest**   | `pytest.ini` sets `DJANGO_SETTINGS_MODULE` + `test_*.py`  |
| **pylint**   | `.pylintrc` loads `pylint_django`, max-line-length=88     |
| **black**    | `pyproject.toml`: line-length=88, target-version=py311     |
| **coverage** | `.coveragerc` omits `*/migrations/*`, `manage.py`, `.venv/`, `*/tests/*` |

## Project layout

- `TheBlogs/` — Django project config (settings, urls, wsgi, asgi)
- `blog/` — the main Django app (models, views, admin scaffolded but empty)
- `db.sqlite3` — SQLite database (gitignored)
- `main.py` — standalone entry point (unrelated to Django)

## Conventions

- `blog` is **not registered** in `INSTALLED_APPS` — add it when wiring up models/views.
- No CI workflows, no pre-commit hooks, no task runner.
- Tests use `pytest-django`; name files `test_*.py`.
- Django's default `SECRET_KEY` from `startproject` is still in `settings.py` — replace for production.
