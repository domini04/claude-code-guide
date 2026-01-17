# Practice Project Guide

How to use this project and understand what Claude Code is doing behind the scenes.

---

## Setup

```bash
cd practice-project
pip install -e ".[dev]"
```

**Verify Setup:**
```bash
uvicorn src.task_manager.main:app --reload  # Should start on :8000
pytest                                       # Should run tests
```

---

## Exercise 1: Memory System

### What to Do
Ask Claude about the project:
- "What is this project?"
- "What commands can I run?"
- "What should I never do in this project?"

### How Claude Code Works
```
1. On startup, Claude scans for CLAUDE.md files:
   ~/.claude/CLAUDE.md        → Global (lowest priority)
   ../CLAUDE.md               → Parent directories
   ./CLAUDE.md                → Project root (this project)
   ./src/CLAUDE.md            → Subdirectories (highest priority)

2. Contents are loaded into Claude's system prompt as instructions

3. When you ask a question, Claude:
   - First checks its loaded CLAUDE.md instructions
   - Then reads relevant files if needed for specifics
   - Answers based on both sources
```

### Verify
Compare Claude's answers against `../PRACTICE_PROJECT_ANSWERS.md` (outside this directory).

---

## Exercise 2: Settings & Permissions

### What to Do
Try these commands and observe behavior:
```bash
# Should work (allowed in settings.json):
pytest --version
ruff --version

# Should be blocked (denied in settings.json):
rm -rf something
```

### How Claude Code Works
```
Settings load order (later overrides earlier):
1. ~/.claude/settings.json           → User defaults
2. .claude/settings.json             → Shared team settings
3. .claude/settings.local.json       → Personal overrides (gitignored)
4. Command-line flags                → Session overrides
5. Enterprise policies               → Cannot be overridden

When Claude tries to run a command:
1. Check against "deny" patterns → Block if matched
2. Check against "allow" patterns → Run without asking if matched
3. If neither → Prompt user for permission
```

### Verify
Look at `.claude/settings.json` to see the allow/deny rules.

---

## Exercise 3: Plan Mode

### What to Do
1. Press `Shift+Tab` twice (or start with `--plan` flag)
2. Ask: "Analyze this codebase and list all issues"
3. Review Claude's plan WITHOUT executing

### How Claude Code Works
```
Plan Mode restricts Claude to read-only tools:
- ✅ Read, Glob, Grep, WebFetch, WebSearch
- ❌ Write, Edit, Bash (execution), Delete

Workflow:
1. Claude explores using read-only tools
2. Creates a plan in a markdown file
3. Presents plan for your approval
4. You approve → Claude exits plan mode and executes
5. You reject → Claude revises the plan
```

### Verify
Claude should identify flaws without changing any files. Check `../PRACTICE_PROJECT_ANSWERS.md` to see if Claude found them all.

---

## Exercise 4: Custom Slash Commands

### What to Do
Type `/` to see available commands, then try:
- `/test` - Run tests
- `/verify` - Full verification suite
- `/review` - Code review

### How Claude Code Works
```
Command discovery:
1. Claude scans .claude/commands/*.md on startup
2. Each file becomes a slash command (filename = command name)
3. The "description" in frontmatter shows in the menu

When you run /test:
1. Claude reads .claude/commands/test.md
2. The markdown content becomes Claude's instructions
3. $ARGUMENTS is replaced with anything after the command
4. Claude executes those instructions

Example: /test routes.py
- Reads test.md
- Replaces $ARGUMENTS with "routes.py"
- Claude runs: pytest routes.py --cov=src -v
```

### Verify
Read `.claude/commands/test.md` to see the instructions Claude receives.

---

## Exercise 5: Hooks (Automation)

### What to Do
1. Ask Claude to edit any Python file
2. Watch the output - ruff should auto-format after the edit

### How Claude Code Works
```
Hook triggers (from settings.json):
- PreToolUse  → Runs BEFORE a tool executes
- PostToolUse → Runs AFTER a tool executes
- Stop        → Runs when Claude finishes a task

Our PostToolUse hook:
{
  "matcher": "Write|Edit",           ← Triggers on Write OR Edit tools
  "hooks": [{
    "type": "command",
    "command": "ruff format $CLAUDE_FILE_PATH..."  ← Runs this
  }]
}

Environment variables available:
- $CLAUDE_FILE_PATH → The file that was edited
- $CLAUDE_TOOL_NAME → Which tool was used
```

### Verify
Make an intentional formatting error. After Claude edits, ruff should fix it automatically.

---

## Exercise 6: Agents

### What to Do
Ask Claude: "Run the code-reviewer agent on routes.py"

### How Claude Code Works
```
Agent discovery:
1. Claude scans .claude/agents/*.md on startup
2. Each file defines a specialized sub-agent

When you invoke an agent:
1. Claude reads the agent's markdown file
2. A NEW Claude instance is spawned with those instructions
3. The sub-agent runs with its own context
4. Results return to the main conversation

Agent file structure:
---
name: code-reviewer
model: opus          ← Can specify different model
---
[Instructions for the agent...]
```

### Verify
The code-reviewer should return structured feedback with Critical/Warning/Suggestion categories.

---

## Exercise 7: Debugging Workflow

### What to Do
1. Run tests: `pytest`
2. If any fail, ask: "Debug this error: [paste error]"
3. Or use: `/debug [paste error]`

### How Claude Code Works
```
Debug workflow (from debug.md command):
1. Parse stack trace → Identify file:line
2. Read the failing code
3. Trace execution path
4. Identify root cause
5. Implement minimal fix
6. Re-run test to verify

Claude uses these tools in sequence:
- Read (examine failing code)
- Grep (find related usages)
- Edit (apply fix)
- Bash (run test again)
```

---

## Exercise 8: TDD Workflow

### What to Do
Ask: "Add a task priority field (high/medium/low) using TDD"

### How Claude Code Works
```
TDD cycle Claude follows:
1. Write failing test first (Write tool → test file)
2. Run test to confirm it fails (Bash tool → pytest)
3. Implement minimal code to pass (Edit tool → source files)
4. Run test to confirm pass (Bash tool → pytest)
5. Refactor if needed (Edit tool)
6. Run all tests (Bash tool → pytest)

The CLAUDE.md verification rules enforce:
- Tests must pass before considering done
- Coverage requirements met
```

---

## Exercise 9: MCP Integration (Optional)

### What to Do
1. Restart Claude Code (to load MCP server)
2. Ask: "Show me all tasks in the database"

### How Claude Code Works
```
MCP (Model Context Protocol) startup:
1. Claude reads .mcp.json
2. Spawns configured servers as subprocesses
3. Servers provide additional tools to Claude

Our sqlite server:
{
  "sqlite": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-sqlite", "tasks.db"]
  }
}

This gives Claude tools like:
- query (run SQL)
- list_tables
- describe_table
```

---

## Quick Reference

| Feature | Location | Trigger |
|---------|----------|---------|
| Memory | CLAUDE.md | Auto-loaded on start |
| Settings | .claude/settings.json | Auto-loaded on start |
| Commands | .claude/commands/*.md | Type `/` |
| Agents | .claude/agents/*.md | "Run the X agent" |
| Hooks | settings.json → hooks | Auto on tool use |
| MCP | .mcp.json | Auto on start (restart needed) |
| Plan Mode | - | Shift+Tab twice |

---

## Verification

Compare Claude's outputs against `../PRACTICE_PROJECT_ANSWERS.md` (intentionally placed outside this directory so Claude can't see it).
