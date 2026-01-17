# Task Manager API

## Overview

A FastAPI REST API for managing tasks. This is a **practice project** with intentional flaws for learning Claude Code workflows.

**Tech Stack**: Python 3.11+, FastAPI, SQLite, Pydantic, pytest

**Architecture**: Simple REST API with SQLite database

## Commands

- **Run server**: `uvicorn src.task_manager.main:app --reload`
- **Run tests**: `pytest --cov=src -v`
- **Lint**: `ruff check src/`
- **Format**: `ruff format src/`
- **Type check**: `mypy src/`

## Code Style

- Use type hints for all function signatures
- Follow PEP 8 naming conventions
- Use Pydantic models for request/response validation
- Prefer composition over inheritance
- Keep functions small and focused

## Verification (REQUIRED)

After ANY code changes, run these checks in order:

1. **Lint**: `ruff check src/` - must pass
2. **Format**: `ruff format --check src/` - must pass
3. **Tests**: `pytest --cov=src` - all must pass
4. **Manual**: Test endpoint in browser or curl if UI-related

Stop at first failure and fix before proceeding.

## Constraints (NEVER DO)

- NEVER commit code that fails tests
- NEVER use raw SQL without parameterization
- NEVER store passwords in plain text
- NEVER expose internal errors to API responses
- NEVER skip input validation on user data
- NEVER use `rm -rf` on project directories

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | List all tasks |
| POST | /tasks | Create a task |
| GET | /tasks/{id} | Get a task by ID |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Known Issues (For Practice)

This codebase has intentional flaws for learning:
- Missing input validation in some routes
- SQL injection vulnerability
- Duplicated code
- Inconsistent error handling
- Incomplete test coverage

Use Claude Code to identify and fix these issues.

## Database

SQLite database at `tasks.db` with schema:
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```
