## ADDED Requirements

### Requirement: Author posts page renders successfully
The system SHALL serve a post list page at `/author/<author_id>/` that returns an HTTP 200 response for existing authors.

#### Scenario: Successful page load
- **WHEN** a client sends a GET request to `/author/1/` for an existing author
- **THEN** the server SHALL respond with status code 200
- **THEN** the response Content-Type SHALL be `text/html`

#### Scenario: Nonexistent author
- **WHEN** a client sends a GET request to `/author/99999/` for an author that does not exist
- **THEN** the server SHALL respond with status code 404

### Requirement: Author posts page displays only that author's posts
The page SHALL display only Post objects whose `author` field matches the given author_id, ordered by `created_at` descending (newest first).

#### Scenario: Author with posts
- **WHEN** author Alice (pk=1) has 3 posts and author Bob (pk=2) has 2 posts
- **THEN** a request to `/author/1/` SHALL show exactly Alice's 3 posts
- **THEN** those posts SHALL be ordered newest first

#### Scenario: Author with no posts
- **WHEN** an author exists but has no posts
- **THEN** the page SHALL render without error showing an empty list

### Requirement: Author posts page shows author name
The page SHALL display the author's name as a heading or label.

#### Scenario: Author name displayed
- **WHEN** viewing the page for author with name "Alice"
- **THEN** the page SHALL contain the text "Alice"

### Requirement: Author posts page uses base template
The page SHALL extend the shared base template.

#### Scenario: Template inheritance
- **WHEN** the author posts page is rendered
- **THEN** the output SHALL include content from `blog/templates/blog/base.html`

### Requirement: Author posts page links to post detail
Each post title on the author posts page SHALL be a hyperlink to that post's detail page.

#### Scenario: Link target
- **WHEN** a post with pk=5 is listed
- **THEN** the title shall be wrapped in an anchor tag pointing to `/post/5/`