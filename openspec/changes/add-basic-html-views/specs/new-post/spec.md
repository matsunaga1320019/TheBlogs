## ADDED Requirements

### Requirement: New post page renders form on GET
The system SHALL serve a new post form at `/new/` that returns an HTTP 200 response with an HTML form containing title and content fields.

#### Scenario: GET request
- **WHEN** a client sends a GET request to `/new/`
- **THEN** the server SHALL respond with status code 200
- **THEN** the response SHALL contain an HTML form with input fields for title and content

### Requirement: New post page creates post on POST
The system SHALL accept a POST request to `/new/` with title and content, create a new Post object, and redirect to the index page.

#### Scenario: Successful post creation
- **WHEN** a client sends a POST request to `/new/` with valid title and content
- **THEN** a new Post object SHALL be created in the database
- **THEN** the server SHALL respond with a redirect (HTTP 302) to `/`

#### Scenario: Author assignment暂定
- **WHEN** a new post is created
- **THEN** the post's author SHALL be set to `Author.objects.first()`

### Requirement: New post page uses base template
The new post page SHALL extend the shared base template.

#### Scenario: Template inheritance
- **WHEN** the new post form page is rendered
- **THEN** the output SHALL include content from `blog/templates/blog/base.html`