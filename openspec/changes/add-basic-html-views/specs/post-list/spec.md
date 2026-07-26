## ADDED Requirements

### Requirement: Post list page renders successfully
The system SHALL serve a post list page at the root URL (`/`) that returns an HTTP 200 response with HTML content.

#### Scenario: Successful page load
- **WHEN** a client sends a GET request to `/`
- **THEN** the server SHALL respond with status code 200
- **THEN** the response Content-Type SHALL be `text/html`

### Requirement: Post list displays all posts
The post list page SHALL display all Post objects ordered by `created_at` descending (newest first).

#### Scenario: Multiple posts exist
- **WHEN** three posts exist with dates Jan 1, Jan 3, Jan 2
- **THEN** the list SHALL show them in order: Jan 3, Jan 2, Jan 1

#### Scenario: No posts exist
- **WHEN** no Post objects exist in the database
- **THEN** the page SHALL render without error

### Requirement: Post list shows post metadata
Each post entry on the list page SHALL display the post title, author name, and creation date.

#### Scenario: Post entry content
- **WHEN** a post with title "Hello", author name "Alice", and created_at "2025-01-15" is rendered
- **THEN** the page SHALL contain the text "Hello"
- **THEN** the page SHALL contain the text "Alice"
- **THEN** the page SHALL contain a formatted representation of "2025-01-15"

### Requirement: Post list links to post detail
Each post title on the list page SHALL be a hyperlink to that post's detail page.

#### Scenario: Link target
- **WHEN** a post with pk=5 is listed
- **THEN** the title shall be wrapped in an anchor tag pointing to `/post/5/`

### Requirement: Post list uses base template
The post list page SHALL extend a shared base template providing the page structure.

#### Scenario: Template inheritance
- **WHEN** the post list page is rendered
- **THEN** the output SHALL include content from `blog/templates/blog/base.html`