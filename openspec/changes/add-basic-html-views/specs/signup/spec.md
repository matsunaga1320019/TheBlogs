## ADDED Requirements

### Requirement: Signup page renders form on GET
The system SHALL serve a signup form at `/signup/` that returns an HTTP 200 response with an HTML form.

#### Scenario: GET request
- **WHEN** a client sends a GET request to `/signup/`
- **THEN** the server SHALL respond with status code 200
- **THEN** the response SHALL contain an HTML form

### Requirement: Signup page redirects on POST
The system SHALL accept a POST request to `/signup/` and redirect to the index page without creating any User or Author objects.

#### Scenario: POST request redirects
- **WHEN** a client sends a POST request to `/signup/`
- **THEN** the server SHALL respond with a redirect (HTTP 302) to `/`

#### Scenario: No user created
- **WHEN** a POST request is made to `/signup/`
- **THEN** no new User object SHALL be created
- **THEN** no new Author object SHALL be created

### Requirement: Signup page uses base template
The signup page SHALL extend the shared base template.

#### Scenario: Template inheritance
- **WHEN** the signup form page is rendered
- **THEN** the output SHALL include content from `blog/templates/blog/base.html`