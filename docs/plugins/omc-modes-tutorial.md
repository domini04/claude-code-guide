# oh-my-claudecode Modes Tutorial

**Plugin**: oh-my-claudecode (OMC) by Yeachan-Heo
**Time**: ~30 minutes

## What You'll Learn

oh-my-claudecode provides multi-agent orchestration modes for autonomous task execution. Each mode optimizes for different goals: speed, cost, reliability, or coordination.

## Mode Overview

| Mode | Keyword | Optimizes For |
|------|---------|---------------|
| autopilot | `autopilot:` | Standard autonomous execution |
| ecomode | `eco:` | Lower token cost (30-50% savings) |
| ralph | `ralph:` | Completion verification |
| ultrapilot | `ulw` | Parallel speed (3-5x faster) |
| swarm | `/swarm` | Coordinated parallel agents |
| pipeline | `/pipeline` | Sequential multi-stage work |

---

## Exercise 1: Autopilot Mode {#autopilot}

### What It Does
Full autonomous execution from start to finish. Claude plans, implements, and verifies without intervention.

### When to Use
- Clear, well-defined tasks
- Single-feature implementations
- Refactoring with clear scope
- Bug fixes with known solutions

### Try It

```
autopilot: create a simple CLI todo app in Python

Requirements:
- Add, list, complete, and delete todos
- Persist to a JSON file
- Use argparse for CLI interface
```

### What to Observe
1. Watch Claude create a plan automatically
2. See files created without prompting
3. Notice verification steps (running the app)
4. Final summary of what was built

### Expected Output
```
practice-project/
├── todo.py          # Main CLI application
├── todos.json       # Data persistence
└── README.md        # Usage documentation (maybe)
```

---

## Exercise 2: Ecomode {#ecomode}

### What It Does
Uses smaller, faster models (Haiku/Sonnet) for subtasks while maintaining quality. Reduces token usage by 30-50%.

### When to Use
- Budget-conscious development
- Large codebases (tokens add up)
- Repetitive tasks
- Non-critical work

### Try It

```
eco: add comprehensive tests to the todo app

Cover all CRUD operations and edge cases.
```

### What to Observe
1. Same quality output as autopilot
2. Lower token consumption
3. Potentially slightly longer wall-clock time
4. Smarter model allocation (Opus for planning, Haiku for execution)

### Cost Comparison

| Mode | Typical Task Cost |
|------|-------------------|
| autopilot: | $0.50-2.00 |
| eco: | $0.20-1.00 |

---

## Exercise 3: Ralph Mode {#ralph}

### What It Does
Loops until the task is **verified complete**. Won't stop until tests pass, builds succeed, or explicit verification criteria are met.

### When to Use
- Critical features that must work
- Bug fixes that need confirmation
- When "almost done" isn't acceptable
- CI-like verification needs

### Try It

```
ralph: refactor the todo app to use SQLite instead of JSON

Ensure all existing tests still pass after migration.
```

### What to Observe
1. Implementation happens normally
2. Verification runs (tests execute)
3. If tests fail, Claude fixes and re-verifies
4. Loop continues until success
5. Clear "verified complete" message

### Ralph vs Autopilot

| Aspect | autopilot | ralph |
|--------|-----------|-------|
| Stops when | Implementation done | Verification passes |
| Handles failures | May leave broken | Fixes until working |
| Token usage | Lower | Higher (loops) |
| Confidence | Medium | High |

---

## Exercise 4: Ultrapilot {#ultrapilot}

### What It Does
Parallel execution across multiple files/features. Partitions work by file ownership to avoid conflicts.

### When to Use
- Multi-file features
- Adding several independent components
- Large refactoring across codebase
- When speed is critical

### Try It

```
ulw add three new features to the todo app in parallel:
1. Priority levels (high/medium/low) with sorting
2. Due dates with overdue highlighting
3. Categories/tags with filtering
```

### What to Observe
1. Work splits across parallel agents
2. Each agent owns specific files
3. Merging happens automatically
4. 3-5x faster than sequential execution

### Parallel Execution Visualization

```
┌─────────────────────────────────────────────┐
│                 Coordinator                  │
└─────────────────┬───────────────────────────┘
                  │ splits work
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌───────┐   ┌───────┐   ┌───────┐
│Agent 1│   │Agent 2│   │Agent 3│
│Priority│  │Due Date│   │Tags   │
└───────┘   └───────┘   └───────┘
    │             │             │
    └─────────────┼─────────────┘
                  ▼ merges results
         ┌─────────────┐
         │   Complete  │
         └─────────────┘
```

---

## Exercise 5: Swarm Mode {#swarm}

### What It Does
Multiple coordinated agents work from a shared task list. Tasks are claimed atomically (SQLite-based) to prevent conflicts.

### When to Use
- Large task backlogs
- Multiple independent work items
- When you want N agents working simultaneously
- Clearing technical debt

### Try It

```
/swarm

Task list:
1. Add input validation to todo.py
2. Add colorized output for different priorities
3. Add export to CSV functionality
4. Add import from CSV functionality
5. Add a "stats" command showing todo metrics
```

### What to Observe
1. Agents claim tasks from shared queue
2. No task is worked on twice
3. Progress visible in real-time
4. Automatic coordination

---

## Exercise 6: Pipeline Mode {#pipeline}

### What It Does
Sequential multi-stage execution where each stage's output feeds the next. Like CI/CD for Claude tasks.

### When to Use
- Dependent tasks (must happen in order)
- Analysis → Implementation → Testing flows
- When one task's output is another's input
- Complex multi-phase work

### Try It

```
/pipeline

Stages:
1. Analyze: Review todo app code and identify improvement opportunities
2. Plan: Create detailed implementation plan for top 3 improvements
3. Implement: Execute the plan
4. Verify: Run tests and validate all improvements work
```

### Pipeline Visualization

```
Stage 1: Analyze    Stage 2: Plan    Stage 3: Implement    Stage 4: Verify
┌──────────────┐   ┌──────────────┐   ┌──────────────┐     ┌──────────────┐
│ Code Review  │──►│ Create Plan  │──►│ Write Code   │────►│ Run Tests    │
│              │   │              │   │              │     │              │
│ Output:      │   │ Output:      │   │ Output:      │     │ Output:      │
│ Issues list  │   │ Plan doc     │   │ Changed files│     │ Test results │
└──────────────┘   └──────────────┘   └──────────────┘     └──────────────┘
```

---

## Mode Selection Guide

```
┌─────────────────────────────────────────────────────────────┐
│                  WHICH MODE SHOULD I USE?                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Single task, clear requirements?                           │
│    └─► autopilot:                                          │
│                                                             │
│  Same task, but budget-conscious?                          │
│    └─► eco:                                                │
│                                                             │
│  Must verify completion (tests must pass)?                 │
│    └─► ralph:                                              │
│                                                             │
│  Multiple independent features (speed priority)?           │
│    └─► ulw (ultrapilot)                                    │
│                                                             │
│  Backlog of many small tasks?                              │
│    └─► /swarm                                              │
│                                                             │
│  Sequential dependent stages?                              │
│    └─► /pipeline                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Patterns

### Pattern 1: Feature Development
```
autopilot: implement user authentication with JWT
```

### Pattern 2: Large Feature, Budget Conscious
```
eco: add comprehensive admin dashboard with user management
```

### Pattern 3: Critical Bug Fix
```
ralph: fix the race condition in user session handling - tests must pass
```

### Pattern 4: Multi-feature Sprint
```
ulw implement all items from this sprint:
- Feature A
- Feature B
- Feature C
```

### Pattern 5: Tech Debt Cleanup
```
/swarm

Clean up these issues:
- Remove unused imports across all files
- Add type hints to public functions
- Update deprecated API calls
- Fix all linting warnings
```

---

## Tips for Success

1. **Start with autopilot**: Learn the autonomous flow before optimizing
2. **Use eco for iteration**: Save budget when experimenting
3. **Ralph for production**: When it must work, use ralph
4. **Clear requirements matter**: All modes work better with specifics
5. **Watch the first run**: Understanding the flow helps you use it better

## Canceling Active Modes

If you need to stop an active mode:

```
/cancel
```

This cleanly terminates autopilot, ralph, ultrapilot, or any other active OMC mode.

---

## Next Steps

1. Start with `autopilot:` on a small, isolated task
2. Compare `eco:` results and costs on the same task
3. Try `ralph:` when you need verified completion
4. Experiment with `ulw` on multi-file features
5. Return to [README.md](README.md) for the full skill progression
