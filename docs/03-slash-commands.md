# Slash Commands: Custom Automations

## What Are Slash Commands?

Slash commands are custom shortcuts stored as markdown files in `.claude/commands/` that automate repeated workflows. They appear in the `/` menu and can include inline bash commands.

Think of them as macros for your most common Claude Code tasks.

## Boris's Most-Used Command

**`/commit-push-pr`**: Runs dozens of times daily by the Claude Code team

This single command:
1. Stages changes
2. Creates commit with proper format
3. Pushes to remote
4. Creates pull request
5. Includes verification steps

## Why Slash Commands Matter

### Without Slash Commands
Every time you want to commit:
```
User: Stage my changes, create a commit following our conventions,
      push to remote, and create a PR with the summary
Claude: [Executes 4 separate steps]
```
Repeated 20+ times daily = inefficient.

### With Slash Commands
```
User: /commit-push-pr
Claude: [Executes entire workflow]
```
One command, consistent results.

## Creating Slash Commands

### Directory Structure
```
.claude/
  commands/
    commit-push-pr.md
    verify-app.md
    update-docs.md
    debug-errors.md
```

### Basic Format

Create a markdown file in `.claude/commands/`:

**File**: `.claude/commands/hello.md`
```markdown
Say hello to the user and show the current date.
```

**Usage**: Type `/hello` in Claude Code

### Command with Instructions

**File**: `.claude/commands/verify-app.md`
```markdown
Verify the application is working correctly:

1. Run the type checker
2. Run all tests
3. Start the dev server
4. Check for console errors
5. Report results with a summary
```

### Command with Inline Bash

**File**: `.claude/commands/status.md`
```markdown
Show the current project status.

Run these commands and summarize:

```bash
git status
git log -1 --oneline
npm test -- --coverage
\`\`\`

Provide a brief summary of the current state.
```

Note: The inline bash is executed automatically.

## Professional Command Examples

### 1. Commit + Push + PR

**File**: `.claude/commands/commit-push-pr.md`
```markdown
Create a commit and pull request following team conventions:

1. Run `git status` and `git diff` to see changes
2. Run `git log -3 --oneline` to review recent commits
3. Stage relevant files with `git add`
4. Create a commit message following our style:
   - Start with type: feat, fix, docs, refactor, test, chore
   - Brief description (present tense)
   - Include "Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
5. Push to remote
6. Create PR with:
   - Clear title
   - Summary of changes
   - Test plan
   - Include "🤖 Generated with Claude Code"
```

### 2. Debug Error Flow

**File**: `.claude/commands/debug-error.md`
```markdown
Debug the current error:

1. Read the error message/stack trace
2. Find the relevant code
3. Identify the root cause
4. Propose a fix
5. Explain why the error occurred
6. Suggest how to prevent similar issues

After proposing, ask if I should implement the fix.
```

### 3. Update Documentation

**File**: `.claude/commands/update-docs.md`
```markdown
Update documentation for recent changes:

1. Review git diff to see what changed
2. Check which docs need updating:
   - README.md
   - API documentation
   - CHANGELOG.md
   - Inline code comments (if complex logic)
3. Update relevant docs
4. Ensure examples still work
5. Update version numbers if needed
```

### 4. Code Review Prep

**File**: `.claude/commands/review-prep.md`
```markdown
Prepare this code for review:

1. Run linter and fix issues
2. Run type checker and fix errors
3. Run tests and ensure they pass
4. Check for:
   - Unused imports
   - Console.logs or debugging code
   - TODOs that should be addressed
   - Missing error handling
5. Verify commit messages follow conventions
6. Create/update tests for new functionality
7. Update CLAUDE.md if new patterns were established
```

### 5. Simplify Code

**File**: `.claude/commands/simplify.md`
```markdown
Simplify the code I'm about to show you:

1. Identify complexity and code smells
2. Suggest simplifications:
   - Remove duplication
   - Extract helper functions
   - Improve naming
   - Reduce nesting
   - Remove unnecessary code
3. Show before/after comparison
4. Explain the benefits

Ask for approval before making changes.
```

### 6. Feature Scaffold

**File**: `.claude/commands/new-feature.md`
```markdown
Scaffold a new feature:

1. Ask me for feature details:
   - Feature name
   - Description
   - Which part of the app (frontend/backend/both)
2. Create the following structure:
   - Main implementation file(s)
   - Test file(s)
   - Update routing/navigation if needed
   - Add to appropriate index/exports
3. Add skeleton code following project patterns
4. Create basic tests
5. Update CLAUDE.md if new patterns introduced
```

### 7. Performance Check

**File**: `.claude/commands/perf-check.md`
```markdown
Check performance of the current code:

```bash
npm run build
ls -lh dist/
\`\`\`

Analyze:
1. Bundle sizes (report in KB/MB)
2. Identify large dependencies
3. Look for:
   - Unnecessary re-renders (React)
   - Expensive operations in loops
   - Missing memoization
   - Inefficient algorithms
4. Suggest specific optimizations
5. Prioritize by impact

Ask before implementing changes.
```

### 8. Quick Test

**File**: `.claude/commands/quick-test.md`
```markdown
Run tests for the current file:

1. Identify the test file for current context
2. Run only those tests
3. If failures, show errors clearly
4. Offer to fix failing tests

```bash
npm test -- <specific-test-file>
\`\`\`
```

## Advanced: Parameterized Commands

You can create commands that prompt for input:

**File**: `.claude/commands/create-component.md`
```markdown
Create a new React component.

Ask me:
1. Component name
2. Should it use TypeScript? (default: yes)
3. Include tests? (default: yes)

Then create:
- Component file in src/components/
- Test file in src/components/__tests__/
- Export from src/components/index.ts
- Basic component structure following our patterns
```

## Commands with Verification

Combine with verification for quality:

**File**: `.claude/commands/safe-refactor.md`
```markdown
Refactor the code safely:

1. Run tests BEFORE changes (capture baseline)
2. Make the refactoring
3. Run tests AFTER changes
4. Compare results - must be identical
5. Run type checker
6. Show diff of changes
7. Confirm no functionality changed
```

## Team Sharing

Check commands into git to share with team:

```bash
git add .claude/commands/
git commit -m "feat: add team slash commands"
git push
```

Team members get commands automatically on pull.

## Command Organization

For large teams, organize by category:

```
.claude/
  commands/
    git/
      commit-push-pr.md
      rebase-interactive.md
    test/
      quick-test.md
      coverage.md
    docs/
      update-docs.md
      api-docs.md
```

Claude Code will show them in submenus.

## Command Best Practices

### 1. Make Them Specific
**Good**: `/commit-push-pr` (clear workflow)
**Bad**: `/git` (too vague)

### 2. Include Verification
```markdown
After making changes:
1. Run type checker
2. Run tests
3. Verify in browser
```

### 3. Follow Team Conventions
Reference CLAUDE.md patterns:
```markdown
Create a commit following our conventions in CLAUDE.md
```

### 4. Use Clear Names
- `/verify-app` not `/v`
- `/update-docs` not `/docs`
- `/debug-error` not `/dbg`

### 5. Add Context
```markdown
# What this command does
This command creates a feature branch, implements the feature,
and creates a PR following team conventions.

# When to use
Use when starting work on a new feature from an issue.

# Steps
...
```

## Common Command Patterns

### Pattern 1: Workflow Automation
```markdown
1. Prepare (run checks, gather info)
2. Execute (main task)
3. Verify (confirm success)
4. Report (summarize results)
```

### Pattern 2: Diagnostic Commands
```markdown
1. Gather information (logs, status, diffs)
2. Analyze (identify issues)
3. Explain (what's wrong and why)
4. Suggest (how to fix)
5. Ask (should I fix it?)
```

### Pattern 3: Generation Commands
```markdown
1. Ask for parameters (name, type, options)
2. Generate files (following patterns)
3. Update exports/imports
4. Create tests
5. Update docs
```

## Command Testing

Test your commands:

1. **Create** the command file
2. **Reload** Claude Code (or restart session)
3. **Type** `/` and find your command
4. **Run** it and observe behavior
5. **Refine** based on results

## Commands vs Skills vs Agents

### Slash Commands
- Simple, prompt-based
- Quick workflows
- Stored as markdown
- No coding required

### Skills (Advanced)
- More complex
- Can include custom code
- Installed separately
- See official docs

### Subagents (Advanced)
- Specialized AI agents
- Long-running tasks
- Pre-built by team
- Examples: `code-simplifier`, `verify-app`

## Discovering Commands

See available commands:
```
User: /
```

Claude Code shows a menu of all commands from:
- Built-in commands
- Your `.claude/commands/`
- Team-shared commands

## Built-in Commands

Claude Code includes built-in commands:
- `/help` - Get help
- `/permissions` - Manage permissions
- `/init` - Initialize CLAUDE.md

Your custom commands extend these.

## Example: Boris's Daily Workflow

```
# Morning
/status                    # Check project state
/quick-test                # Verify tests passing

# During work
/debug-error               # Fix issue
/verify-app                # Check changes
/commit-push-pr            # Ship it

# Code review
/review-prep               # Prepare for review
/simplify                  # Clean up code
```

Running these commands 20-30 times daily - automation saves hours.

## Building Your Command Library

### Start Small
Begin with your most repeated task:
1. Notice "I keep asking Claude to do X"
2. Create `/x` command
3. Refine over a week
4. Share with team

### Grow Organically
Add commands as needs arise:
- Week 1: `/commit-push-pr`
- Week 2: `/verify-app`
- Week 3: `/debug-error`
- Week 4: `/update-docs`

### Measure Impact
Track how often you use each command. Keep high-value commands, remove unused ones.

## Troubleshooting

### Command not appearing
1. Check file is in `.claude/commands/`
2. Check file extension is `.md`
3. Restart Claude Code session
4. Verify no syntax errors in markdown

### Command not working as expected
1. Test inline bash separately
2. Simplify command to debug
3. Add explicit steps
4. Check CLAUDE.md for conflicts

### Command too verbose
1. Remove unnecessary explanation
2. Use bullet points, not paragraphs
3. Focus on actions, not context

## Next Steps

1. **Create your first command**: Start with `/verify-app`
2. **Test it**: Run multiple times, refine
3. **Build your library**: Add 1 command per week
4. **Share with team**: Check into git
5. **Combine with hooks**: See [04-hooks-automation.md](04-hooks-automation.md)

## Resources

- [Claude Code Commands Docs](https://code.claude.com/docs/commands)
- [Community Command Examples](https://github.com/ChrisWiles/claude-code-showcase)
- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
