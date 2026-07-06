## ADDED Requirements

### Requirement: Project has opencode configuration
The project SHALL include an opencode.json (or opencode.jsonc) file at the repository root that governs agent behavior.

#### Scenario: Configuration file exists
- **WHEN** the agent reviews the project root
- **THEN** it SHALL find an opencode.json or opencode.jsonc file

#### Scenario: Configuration is valid JSON
- **WHEN** the configuration file is parsed
- **THEN** it SHALL parse without errors

### Requirement: Configuration governs agent permissions
The opencode configuration SHALL specify which directories the agent may read and write, and which shell commands require user approval.

#### Scenario: Permissions are defined
- **WHEN** the agent validates a shell command against the configuration
- **THEN** the configuration SHALL determine whether the command runs automatically or requires user approval

#### Scenario: Allowed paths are scoped
- **WHEN** the agent attempts to edit files
- **THEN** edits SHALL be constrained to paths declared in the configuration

### Requirement: Configuration is gitignored appropriately
The `.opencode/` directory contents (node_modules, package-lock.json) MAY be gitignored to avoid committing build artifacts.

#### Scenario: node_modules excluded
- **WHEN** running `git status`
- **THEN** the `.opencode/node_modules/` directory SHALL NOT appear as untracked
