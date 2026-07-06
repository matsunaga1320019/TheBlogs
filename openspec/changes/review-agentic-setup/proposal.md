## Why

The current AI agentic setup for TheBlogs is functional but lacks several pieces needed for a smooth, consistent developer experience. AGENTS.md documents the toolchain but doesn't reflect the openspec workflow or the installed skills. The `blog` app is scaffolded but not wired into `INSTALLED_APPS`, no models/views exist, and the agent has no opencode configuration file to govern its behavior. A review will close these gaps and ensure the agent setup is production-ready.

## What Changes

1. **Update AGENTS.md** to add openspec workflow commands (`/opsx:propose`, `/opsx-apply`, etc.) and document all installed skills (django-expert, openspec skills).
2. **Add opencode.json** config file at the project root to govern agent behavior (permission patterns, allowed edit paths, etc.).
3. **Register `blog` app** in INSTALLED_APPS so Django recognises it.
4. **Align django-expert skill** references to match the actual Django version (5.2.x) and project conventions.
5. **Install missing skill** — determine if `code-reviewer`, `receiving-code-review`, or `refactordjango` skills should be added and install those that add value.
6. **Add `.opencode/` directory to `.gitignore`**? — review whether node_modules and package-lock.json in `.opencode/` should be gitignored or not.
7. **Add a basic smoke test** so the agent can verify the setup works end-to-end.

## Capabilities

### New Capabilities
- `agent-config`: OpenCode configuration file and agent behavior governance
- `agents-md-docs`: Maintained AGENTS.md with accurate workflow and skill documentation
- `app-wiring`: Django app registration and basic project bootstrapping

### Modified Capabilities

- None — no existing specs at `openspec/specs/`

## Impact

- `AGENTS.md` — updated documentation
- `opencode.json` — new config file at project root
- `TheBlogs/settings.py` — add `blog` to INSTALLED_APPS
- `.agents/skills/django-expert/SKILL.md` — minor version references
- `.gitignore` — potentially add `.opencode/node_modules/`
