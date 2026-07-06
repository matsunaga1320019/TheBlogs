## ADDED Requirements

### Requirement: AGENTS.md documents all workflows
AGENTS.md SHALL include command examples for the openspec workflow (`/opsx:propose`, `/opsx-apply`, `/opsx-archive`, `/opsx-explore`, `/opsx-sync`).

#### Scenario: Workflow commands documented
- **WHEN** a developer reads AGENTS.md
- **THEN** they SHALL find examples of all openspec workflow commands

### Requirement: AGENTS.md lists installed skills
AGENTS.md SHALL list all installed agent skills (django-expert, openspec skills) with a brief description of each.

#### Scenario: Skills inventory present
- **WHEN** a developer reads AGENTS.md
- **THEN** they SHALL find a section listing installed skills

### Requirement: AGENTS.md toolchain is accurate
The toolchain table in AGENTS.md SHALL match the actual project configuration files (pyproject.toml, pytest.ini, .pylintrc, .coveragerc, .python-version).

#### Scenario: Tool versions are correct
- **WHEN** comparing AGENTS.md to pyproject.toml
- **THEN** all tool versions and notes SHALL be accurate
