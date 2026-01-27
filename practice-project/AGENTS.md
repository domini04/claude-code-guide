# AGENTS.md - Practice Project

## Purpose
FastAPI REST API with intentional flaws for learning Claude Code workflows.

## Behavior Guidelines
- EXPLAIN flaws before fixing them (educational context)
- FIX one issue at a time for learning clarity
- RUN verification after every change
- USE parameterized queries - this codebase has SQL injection examples

## Verification
- After code changes: `pytest --cov=src -v`
- After route changes: `pytest tests/test_api.py -v`
- Lint check: `ruff check src/`

## Known Issues (Intentional)
These exist for learning - don't auto-fix without explanation:
- SQL injection vulnerability in database.py
- Missing input validation in routes
- Duplicated code patterns
- Inconsistent error handling

## Exercise Tracking
See GUIDE.md for 9 structured exercises covering:
1. Memory/context (CLAUDE.md)
2. Settings management
3. Plan Mode
4. Custom commands
5. Hooks automation
6. Permissions
7. Verification
8. MCP integration
9. Parallel sessions

## Related
- Exercise guide: `GUIDE.md`
- Project CLAUDE.md: `CLAUDE.md`
