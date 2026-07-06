## Context

TheBlogs is a fresh Django 5.2.15 project managed with `uv`. The project has an AGENTS.md that documents the basic toolchain but doesn't cover the openspec workflow commands or installed agent skills. The `blog` Django app is scaffolded but not registered in INSTALLED_APPS. There is no `opencode.json` configuration file to govern agent behavior. The `.opencode/` directory contains `node_modules/` and `package-lock.json` from the openspec plugin dependency — these are build artifacts that should likely be gitignored to avoid cluttering the repo.

## Goals / Non-Goals

**Goals:**
- Update AGENTS.md to document all available openspec workflow commands and installed skills
- Create `opencode.json` at the project root to govern agent permissions and edit scopes
- Register `blog` app in `INSTALLED_APPS`
- Add `.opencode/node_modules/` and `.opencode/package-lock.json` to `.gitignore`
- Add a basic smoke test to verify the project boots correctly
- Update django-expert skill references from Django 5.0 → 5.2

**Non-Goals:**
- Implementing any blog features (models, views, URLs)
- Adding DRF or other new dependencies
- Setting up CI/CD pipelines
- Configuring production deployment settings

## Decisions

1. **opencode.json format**: Use JSON (not JSONC) for simplicity. Place at repo root. Include `agentSettings` for approval patterns and `allowedEditRoots` constraint.
2. **AGENTS.md structure**: Keep the existing Quick start + Toolchain + Project layout sections. Add two new sections: "Workflow Commands" and "Installed Skills".
3. **Smoke test location**: Place in `blog/tests.py` using Django's `SimpleTestCase` to verify app loading without needing a database.
4. **`blog` app position**: Add after `"django.contrib.staticfiles"` in INSTALLED_APPS, following Django convention of third-party after built-in, first-party after third-party.
5. **Gitignore entries**: No changes needed — `node_modules/` is already covered by the `.venv/` pattern convention, but `.opencode/node_modules/` is a specific path that should be explicitly listed.

## Risks / Trade-offs

- [Risk] `opencode.json` schema may change between versions → Mitigation: use minimal configuration that's stable across versions
- [Risk] django-expert skill references Django 5.0 patterns that may differ from 5.2 → Mitigation: review and update only the version reference; the API surface is largely compatible
- [Risk] Adding `blog` to INSTALLED_APPS without any models is harmless but triggers migration creation if any model is added later → This is expected behavior
