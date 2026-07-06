## 1. Agent Configuration

- [ ] 1.1 Create `opencode.json` at project root with agent permission settings and allowed edit paths
- [ ] 1.2 Add `.opencode/node_modules/` and `.opencode/package-lock.json` to `.gitignore`

## 2. Documentation Updates

- [ ] 2.1 Update AGENTS.md — add "Workflow Commands" section with openspec commands (/opsx:propose, /opsx-apply, /opsx-archive, /opsx-explore, /opsx-sync)
- [ ] 2.2 Update AGENTS.md — add "Installed Skills" section listing django-expert and all openspec skills with descriptions
- [ ] 2.3 Verify AGENTS.md toolchain table matches actual configs (pyproject.toml, pytest.ini, .pylintrc, .coveragerc, .python-version)

## 3. Django App Wiring

- [ ] 3.1 Add `"blog"` to `INSTALLED_APPS` in `TheBlogs/settings.py`
- [ ] 3.2 Run `uv run python manage.py check` to verify no errors

## 4. Smoke Test

- [ ] 4.1 Write a `SimpleTestCase` in `blog/tests.py` that imports the settings module and verifies `INSTALLED_APPS` includes `"blog"`
- [ ] 4.2 Run `uv run pytest` to confirm tests pass

## 5. Skill Alignment

- [ ] 5.1 Review django-expert SKILL.md — update Django version references from 5.0 to 5.2 if applicable
- [ ] 5.2 Review project for missing valuable skills (code-reviewer, refactordjango) — install if beneficial
