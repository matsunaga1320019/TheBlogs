# Author Model

## Purpose

Provides an Author model linked to Django's User model for blog authors. TBD.

## Requirements

### Requirement: Author model exists
The system SHALL provide an Author model linked to Django's built-in User model via a OneToOneField. The Author model SHALL have a `name` CharField for display purposes.

#### Scenario: Author model fields
- **WHEN** inspecting the Author model
- **THEN** it SHALL have a `user` field of type `OneToOneField(User, on_delete=models.CASCADE)`
- **THEN** it SHALL have a `name` field of type `CharField(max_length=100)`

### Requirement: Author model string representation
The Author model SHALL implement `__str__()` that returns the author's display `name`.

#### Scenario: Author string representation
- **WHEN** calling `str(author)` on an Author instance
- **THEN** it SHALL return the value of the `name` field

### Requirement: Author registered in admin
The Author model SHALL be registered with Django's admin site via `blog/admin.py`.

#### Scenario: Author appears in admin
- **WHEN** loading the Django admin index page
- **THEN** the Author model SHALL be listed under the Blog section
