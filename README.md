# The Blogs

A shared blog platform built with Django for the Web Engineering (SE01) course project.

## Overview
Users can read blog posts freely. Registered users can write posts.
Posts can be searched by title and filtered by author or date.

## Environment
- Python 3.11
- Django
- Package manager: uv

## Setup
\`\`\`bash
uv sync
uv run manage.py migrate
uv run manage.py runserver
\`\`\`

## Tools
- Black — formatting: `uv run black .`
- Pylint (+ pylint-django) — linting: `uv run pylint blog`
- pytest (+ pytest-django) — testing: `uv run pytest`
- coverage.py — test coverage: `uv run coverage run -m pytest && uv run coverage report`