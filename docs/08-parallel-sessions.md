# Parallel Sessions: Scaling Claude Code

## Boris's Parallel Setup

Boris Cherny runs **5 Claude Code sessions** in parallel in his terminal (numbered 1-5), supplemented by **5-10 additional web sessions** on claude.ai/code.

**Total**: 10-15 concurrent Claude sessions working on different aspects of projects.

## Why Run Parallel Sessions?

### The Problem with Single Sessions
```
Working on Task A → Blocked, need to debug
Can't start Task B while waiting
Can't work on Task C in different context
```

### The Solution: Parallel Sessions
```
Session 1: Implementing feature A
Session 2: Debugging issue B
Session 3: Writing tests for C
Session 4: Updating documentation
Session 5: Code review prep
```

**Result**: Continuous progress across multiple concerns.

## Session Organization Strategies

### Strategy 1: By Component

```
Terminal Tab 1: Frontend (web app)
Terminal Tab 2: Backend (API)
Terminal Tab 3: Database (migrations)
Terminal Tab 4: Tests
Terminal Tab 5: Documentation/Tooling
```

### Strategy 2: By Task Type

```
Session 1: Feature implementation
Session 2: Bug fixes
Session 3: Refactoring
Session 4: Testing
Session 5: Code review/QA
```

### Strategy 3: By Priority

```
Session 1: Urgent production issue
Session 2: High priority feature
Session 3: Medium priority improvements
Session 4: Low priority refactoring
Session 5: Exploration/research
```

### Strategy 4: By Workflow Stage

```
Session 1: Planning (Plan Mode)
Session 2: Implementation
Session 3: Testing
Session 4: Code review prep
Session 5: Documentation updates
```

## Setting Up Parallel Sessions

### Terminal-Based (Boris's Method)

**Using separate git checkouts**:
```bash
# Project root
mkdir -p ~/workspaces/myproject

# Create 5 separate clones
git clone repo ~/workspaces/myproject/session-1
git clone repo ~/workspaces/myproject/session-2
git clone repo ~/workspaces/myproject/session-3
git clone repo ~/workspaces/myproject/session-4
git clone repo ~/workspaces/myproject/session-5

# Open terminals
# Terminal 1: cd ~/workspaces/myproject/session-1 && claude
# Terminal 2: cd ~/workspaces/myproject/session-2 && claude
# ... etc
```

**Why separate clones?** Avoids git conflicts between sessions.

### Using tmux

```bash
# Create tmux session with 5 windows
tmux new-session -s claude \; \
  split-window -h \; \
  split-window -v \; \
  select-pane -t 0 \; \
  split-window -v \; \
  select-pane -t 2 \; \
  split-window -v

# In each pane
cd session-N && claude
```

### Using Terminal Tabs

**iTerm2 / macOS Terminal**:
```
Cmd+T: New tab
Cmd+1-5: Switch between tabs
Label tabs: Session 1, Session 2, etc.
```

**VS Code Integrated Terminal**:
```
Ctrl+Shift+`: New terminal
Rename terminals: "Frontend", "Backend", etc.
```

### Web Sessions (claude.ai/code)

Boris supplements with 5-10 web sessions:

**Benefits**:
- No local setup needed
- Different project contexts
- Easy to access from phone
- Can teleport to local sessions

**Use `--teleport`** to move context between web and local.

## System Notifications

Boris uses system notifications to know when sessions need input.

### macOS Setup

```bash
# In .claude/settings.json
{
  "notifications": {
    "enabled": true,
    "onAgentComplete": true,
    "onUserInputNeeded": true
  }
}
```

Or use terminal notification:
```bash
# After long-running command
claude "Run tests" && osascript -e 'display notification "Tests complete" with title "Session 3"'
```

### Linux Setup

```bash
# Using notify-send
claude "Run tests" && notify-send "Session 3" "Tests complete"
```

## Session Coordination

### Problem: Sessions Working on Same Files

**Solution 1**: Separate directories (Boris's approach)
- Each session has its own git clone
- No file conflicts
- Merge changes via git

**Solution 2**: Different branches
```
Session 1: feature/authentication
Session 2: feature/dark-mode
Session 3: bugfix/checkout-error
Session 4: refactor/api-client
Session 5: main (for quick fixes)
```

**Solution 3**: File-level coordination
Document in CLAUDE.md:
```markdown
# Parallel Session Coordination

Current work assignments:
- Session 1: src/auth/* (authentication feature)
- Session 2: src/ui/theme/* (dark mode)
- Session 3: src/checkout/* (bug fix)
- Session 4: tests/* (test improvements)
- Session 5: docs/* (documentation)
```

## Background Operations

Use `&` to run sessions in background:

```bash
# Start session in background
claude "Implement authentication feature" &

# Continue with other work
# Notification when complete
```

Or use `--teleport`:
```bash
# Start on web
claude.ai/code: "Implement feature"

# Move to local when ready
claude --teleport [session-id]
```

## Parallel Session Workflows

### Workflow 1: Feature Pipeline

```
Session 1 (Plan): Design authentication approach
↓
Session 2 (Implement): Write auth code
↓
Session 3 (Test): Create test suite
↓
Session 4 (Verify): Run tests, check quality
↓
Session 5 (Ship): Create PR, deploy
```

Run all in parallel, each picks up where previous left off.

### Workflow 2: Multi-Component Feature

```
Session 1: Backend API endpoints
Session 2: Frontend UI components
Session 3: Database migrations
Session 4: Integration tests
Session 5: Documentation

All working simultaneously on different parts.
```

### Workflow 3: Investigation & Fix

```
Session 1: Investigate production errors (Sentry MCP)
Session 2: Reproduce bug locally
Session 3: Implement fix
Session 4: Write regression test
Session 5: Prepare deployment

Pipeline approach for fast incident resolution.
```

### Workflow 4: Code Review Prep

```
Session 1: Run linter, fix issues
Session 2: Run tests, fix failures
Session 3: Update documentation
Session 4: Simplify complex code
Session 5: Create PR with summary
```

## Naming and Labeling Sessions

### Descriptive Names

```
✅ "Frontend - Dark Mode"
✅ "Backend - Auth API"
✅ "Tests - Integration"
✅ "Docs - API Reference"
✅ "Debug - Checkout Error"

❌ "Session 1"
❌ "Claude"
❌ "Terminal"
```

### Color Coding (iTerm2)

```
Session 1 (Frontend): Blue
Session 2 (Backend): Green
Session 3 (Tests): Yellow
Session 4 (Docs): Purple
Session 5 (Debug): Red
```

## Session Templates

Create templates for common session types:

### Template 1: Feature Session

```markdown
# Feature Session Template

1. Enter Plan Mode (Shift+Tab twice)
2. Design implementation approach
3. Implement with verification
4. Write tests
5. Update CLAUDE.md if needed
6. Create PR
```

### Template 2: Debug Session

```markdown
# Debug Session Template

1. Read error logs (Sentry MCP or local)
2. Reproduce bug
3. Identify root cause
4. Implement fix with regression test
5. Verify fix works
6. Document in commit message
```

### Template 3: Refactor Session

```markdown
# Refactor Session Template

1. Run tests BEFORE (baseline)
2. Make refactoring changes
3. Run tests AFTER (must match)
4. Verify no behavior change
5. Check performance
6. Update docs if patterns changed
```

## Managing Session Context

### Problem: Forgetting What Each Session Is Doing

**Solution**: Session status file

Create `.claude/session-status.md`:
```markdown
# Active Sessions

## Session 1: Frontend - Dark Mode
Status: Implementing theme toggle component
Branch: feature/dark-mode
Progress: 60% - component done, need to wire up state

## Session 2: Backend - Auth API
Status: Writing tests for JWT validation
Branch: feature/auth
Progress: 80% - implementation done, tests in progress

## Session 3: Debug - Checkout Bug
Status: Investigating null pointer in payment processing
Branch: bugfix/checkout-null
Progress: 40% - reproduced bug, working on fix

## Session 4: Tests
Status: Adding integration tests for API
Branch: test/integration
Progress: 30% - test framework set up

## Session 5: Docs
Status: Updating API documentation
Branch: docs/api-v2
Progress: 70% - most endpoints documented
```

Update this file as sessions progress.

## Phone Integration

Boris mentions starting sessions from his phone daily.

**Use Cases**:
- Start a session while commuting
- Review code on the go
- Check progress of background tasks
- Quick bug investigations

**How**: Use claude.ai/code on mobile browser, then `--teleport` to desktop when needed.

## Session Limits

**Boris runs**: 5 terminal + 5-10 web = 10-15 sessions

**Recommended starting point**: 2-3 sessions

**Scale up gradually**:
- Week 1: 1 session (learn basics)
- Week 2: 2 sessions (try parallel work)
- Week 3: 3-5 sessions (find your workflow)
- Month 2+: 5-10+ sessions (professional setup)

## Monitoring Sessions

### Dashboard Approach

Create a simple dashboard:

```bash
# .claude/session-monitor.sh
#!/bin/bash

echo "=== Claude Code Sessions ==="
echo ""
for i in {1..5}; do
  cd ~/workspaces/myproject/session-$i
  echo "Session $i: $(git branch --show-current)"
  echo "Status: $(git status --short | wc -l) changes"
  echo ""
done
```

Run: `bash .claude/session-monitor.sh`

### Visual Monitoring

Use tools like `tmux` with status bar showing session info.

## Session Best Practices

### 1. One Context Per Session

Don't mix concerns:
```
❌ Session 1: Frontend AND backend AND tests
✅ Session 1: Frontend only
✅ Session 2: Backend only
✅ Session 3: Tests only
```

### 2. Clean Session Boundaries

Avoid dependencies between sessions:
```
❌ Session 1 depends on Session 2's work
✅ Sessions work on independent components
```

Or use sequential workflow:
```
✅ Session 1 → Session 2 → Session 3 (pipeline)
```

### 3. Document Session Purpose

At start of each session:
```
User: This session is for implementing dark mode in the UI.
      All other concerns should be deferred to other sessions.
```

### 4. Close Finished Sessions

Don't let sessions accumulate:
```
Session complete → Merge PR → Close session
Open new session for next task
```

### 5. Periodic Synchronization

Once daily, sync all sessions:
```bash
# Sync all sessions with main
for i in {1..5}; do
  cd ~/workspaces/myproject/session-$i
  git pull origin main
  git rebase main
done
```

## Advanced: Session Orchestration

For very large projects, orchestrate sessions:

```bash
# Orchestration script
#!/bin/bash

# Session 1: Backend
cd session-1 && claude "Implement API endpoints" &

# Wait for API to be ready
sleep 60

# Session 2: Frontend (depends on API)
cd session-2 && claude "Implement UI using new API" &

# Session 3: Tests (depends on both)
sleep 60
cd session-3 && claude "Write integration tests" &

# Session 4: Docs
cd session-4 && claude "Update API documentation" &
```

## Troubleshooting

### Problem: Lost track of what each session is doing

**Solution**: Session status file (see above)

### Problem: Git conflicts between sessions

**Solution**: Separate git clones or different branches

### Problem: Too many sessions, overwhelming

**Solution**: Reduce to 2-3 sessions, focus on high-value work

### Problem: Notifications not working

**Solution**: Check notification permissions, test notification command manually

## Measuring Productivity

Track how parallel sessions improve productivity:

**Single Session**:
- 1 feature per day
- Blocked time when waiting for tests
- Context switching within session

**5 Parallel Sessions**:
- 3-5 features per day
- No blocked time (other sessions continue)
- Clean context per session

**Estimated improvement**: 2-3x productivity boost

## Next Steps

1. **Start with 2 sessions**: One for implementation, one for testing
2. **Observe workflow**: Where do you get blocked?
3. **Add third session**: For debugging or docs
4. **Scale gradually**: Add sessions as needed
5. **Find your optimal**: Boris uses 10-15, yours might be different

## Resources

- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- tmux guide: https://github.com/tmux/tmux/wiki
- iTerm2: https://iterm2.com/
