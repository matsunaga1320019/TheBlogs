## ADDED Requirements

### Requirement: Post detail page renders successfully
The system SHALL serve a post detail page at `/post/<pk>/` that returns an HTTP 200 response for existing posts.

#### Scenario: Successful page load
- **WHEN** a client sends a GET request to `/post/1/` for an existing post
- **THEN** the server SHALL respond with status code 200
- **THEN** the response Content-Type SHALL be `text/html`

#### Scenario: Nonexistent post
- **WHEN** a client sends a GET request to `/post/99999/` for a post that does not exist
- **THEN** the server SHALL respond with status code 404

### Requirement: Post detail displays full content
The post detail page SHALL display the post title, full content, author name, and creation date.

#### Scenario: Detail page content
- **WHEN** a post with title "Hello World", content "Full body text", author "Alice", created_at "2025-01-15" is viewed
- **THEN** the page SHALL contain the text "Hello World"
- **THEN** the page SHALL contain the text "Full body text"
- **THEN** the page SHALL contain the text "Alice"
- **THEN** the page SHALL contain a formatted representation of "2025-01-15"

### Requirement: Post detail uses base template
The post detail page SHALL extend the shared base template.

#### Scenario: Template inheritance
- **WHEN** the post detail page is rendered
- **THEN** the output SHALL include content from `blog/templates/blog/base.html`

### Requirement: Post detail links back to list
The post detail page SHALL include a link back to the post list page.

#### Scenario: Back link
- **WHEN** viewing a post detail page
- **THEN** the page SHALL contain a hyperlink pointing to `/`