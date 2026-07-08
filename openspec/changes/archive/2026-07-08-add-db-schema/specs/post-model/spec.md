## ADDED Requirements

### Requirement: Post model exists
The system SHALL provide a Post model with `title` (CharField), `content` (TextField), `created_at` (DateTimeField with `auto_now_add=True`), and an `author` ForeignKey to the Author model with `on_delete=models.CASCADE`.

#### Scenario: Post model fields
- **WHEN** inspecting the Post model
- **THEN** it SHALL have a `title` field of type `CharField(max_length=200)`
- **THEN** it SHALL have a `content` field of type `TextField`
- **THEN** it SHALL have a `created_at` field of type `DateTimeField` with `auto_now_add=True`
- **THEN** it SHALL have an `author` field of type `ForeignKey(Author, on_delete=models.CASCADE)`

### Requirement: Post model default ordering
The Post model SHALL default to ordering by `created_at` descending (newest first).

#### Scenario: Default ordering
- **WHEN** querying posts without an explicit `.order_by()`
- **THEN** posts SHALL be returned in descending order of `created_at`

### Requirement: Post model string representation
The Post model SHALL implement `__str__()` that returns the post's `title`.

#### Scenario: Post string representation
- **WHEN** calling `str(post)` on a Post instance
- **THEN** it SHALL return the value of the `title` field

### Requirement: Post registered in admin
The Post model SHALL be registered with Django's admin site via `blog/admin.py`.

#### Scenario: Post appears in admin
- **WHEN** loading the Django admin index page
- **THEN** the Post model SHALL be listed under the Blog section
