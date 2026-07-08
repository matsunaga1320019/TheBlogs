# Project: The Blogs

A shared blog platform built with Django.

## Overview

- Anyone can read posts.
- Registered users can write posts.
- Users can search posts by title, filter by author, filter by date.

## Data Model

```
User (Django built-in) —1:1— Author —1:N— Post
```

- **Author** — OneToOne to `User`, has a `name` field.
- **Post** — `title`, `content`, `created_at` (auto), `author` (FK to Author), default ordering newest first.

## Tech Stack

| Layer         | Tool                                                  |
|---------------|-------------------------------------------------------|
| Language      | Python 3.11                                           |
| Framework     | Django 5.2                                            |
| Package mgmt  | `uv`                                                  |
| Database      | SQLite (dev)                                          |
| Tests         | pytest + pytest-django                                |
| Linting       | pylint + pylint-django                                |
| Formatting    | black (line-length 88)                                |

## Conventions

- `blog/` is the main Django app.
- Settings module: `TheBlogs.settings`.
- Test files named `test_*.py`.
