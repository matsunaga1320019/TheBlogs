## ADDED Requirements

### Requirement: `blog` app is registered in INSTALLED_APPS
The `blog` Django application SHALL be registered in `TheBlogs/settings.py` under INSTALLED_APPS.

#### Scenario: blog app registered
- **WHEN** Django loads the settings
- **THEN** INSTALLED_APPS SHALL include `"blog"`

### Requirement: smoke test passes
A basic Django smoke test SHALL exist that verifies the project boots without errors.

#### Scenario: Smoke test runs
- **WHEN** running `uv run pytest`
- **THEN** the smoke test SHALL pass without failures

#### Scenario: Migration check succeeds
- **WHEN** running `uv run python manage.py check --deploy`
- **THEN** no critical errors SHALL be reported
