# Practice Project - Ground Truth Reference

**FOR HUMAN REFERENCE ONLY** - This file is placed outside the practice-project directory so Claude cannot see it when working there. Use this to verify Claude's analysis.

---

## Codebase Summary

A FastAPI REST API for task management with SQLite storage.

**Files:**
- `main.py` - App entry, mounts routes, initializes DB
- `models.py` - 3 Pydantic models (TaskCreate, TaskUpdate, Task)
- `database.py` - 7 functions for SQLite CRUD operations
- `routes.py` - 6 endpoints + 1 unused helper function

**Endpoints:**
| Method | Path | Function |
|--------|------|----------|
| GET | / | root info |
| GET | /health | health check |
| GET | /tasks | list all |
| GET | /tasks/search?q= | search by title |
| POST | /tasks | create |
| GET | /tasks/{id} | get one |
| PUT | /tasks/{id} | update |
| DELETE | /tasks/{id} | delete |

---

## Intentional Flaws (Complete List)

### Security Issues
1. **SQL Injection** - `database.py:37` - `search_tasks()` uses f-string: `f"SELECT * FROM tasks WHERE title LIKE '%{query}%'"`

### Code Quality Issues
2. **Duplicated Code** - `routes.py:17,33,49,63,82` - Task dict conversion repeated 5 times instead of using `convert_task_row()` helper at line 99
3. **Unused Helper** - `routes.py:99` - `convert_task_row()` exists but is never called
4. **Missing Type Hints** - `routes.py:98` - `convert_task_row(row)` has no type annotations

### Error Handling Issues
5. **Inconsistent Error Messages** - `routes.py:89` says `"not found"` (lowercase) vs `routes.py:58,72` says `"Task not found"`
6. **Inconsistent Response Format** - `routes.py:92` returns `{"message": "Task deleted"}` while other endpoints return task objects
7. **Silent Failures** - `database.py:82` - `delete_task()` succeeds even if task doesn't exist (checked in route, but DB doesn't verify)

### Missing Validation
8. **No Title Validation** - No length limit, empty string allowed
9. **No Search Input Sanitization** - `routes.py:29` passes user input directly to vulnerable function

### Architecture Issues
10. **Hardcoded DB Path** - `database.py:8` - `DATABASE_PATH = "tasks.db"`
11. **No Lifecycle Management** - `main.py:14` - DB init runs on import, not in lifespan handler
12. **No CORS Configuration** - `main.py:11` - Missing CORS middleware
13. **Fake Health Check** - `main.py:26` - Returns "healthy" without checking DB connectivity

---

## Test Coverage Gaps

**Missing Tests:**
- Empty title creation
- Very long title
- Special characters in title
- Update completion status
- Update description only
- Update nonexistent task
- Delete nonexistent task
- All search functionality
- SQL injection attempts
- Invalid ID types

**Current Coverage:** ~60% (varies by run)

---

## Settings Configuration

**`.claude/settings.json`** (shared):
- Allows: pytest, ruff, mypy, uvicorn, git commands
- Denies: rm -rf, sudo, chmod 777
- Hook: Auto-formats .py files after Write/Edit

**`.claude/settings.local.json`** (personal):
- Sets model to opus
- Allows curl/http commands

---

## Custom Commands

| Command | Purpose |
|---------|---------|
| /test | Run pytest with coverage |
| /verify | Full lint→format→type→test pipeline |
| /review | Structured code review |
| /debug | Systematic debugging workflow |

---

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| code-reviewer | opus | Security + quality review with severity levels |
| test-runner | haiku | Run tests and analyze coverage |
