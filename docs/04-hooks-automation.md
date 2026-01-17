# Hooks & Automation

## What Are Hooks?

Hooks are automated actions triggered by specific events in Claude Code. They run commands or scripts in response to tool usage, allowing you to automate repetitive tasks without manual intervention.

**Key insight**: "Never send an LLM to do a linter's job" - Use hooks for deterministic tasks.

## Types of Hooks

### 1. PostToolUse
Runs after Claude uses specific tools (Write, Edit, Bash, etc.)

### 2. PrePromptSubmit
Runs before sending your message to Claude

### 3. AgentStop
Runs when a background agent completes

## Boris's Hook Setup

Boris's team uses PostToolUse hooks extensively, especially for code formatting:

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "bun run format || true"
    }]
  }]
}
```

**Result**: Code is automatically formatted after every edit, catching edge cases Claude might miss.

## Why Hooks Matter

### Without Hooks
```
Claude: [Writes code]
User: Can you format that?
Claude: [Runs formatter]
User: Also run the linter
Claude: [Runs linter]
User: And type check
Claude: [Runs type checker]
```

### With Hooks
```
Claude: [Writes code]
Hook: [Auto-formats, lints, and type checks]
Result: Ready for commit
```

## PostToolUse Hooks

### Basic Format

Configuration in `.claude/settings.json`:

```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "command",
          "command": "npm run format"
        }
      ]
    }
  ]
}
```

### Anatomy

- **matcher**: Regex pattern for tool names (Write, Edit, Bash, etc.)
- **hooks**: Array of commands to run
- **type**: "command" (shell command)
- **command**: The actual command to execute

### Common Matchers

```json
"matcher": "Write"          // Only Write tool
"matcher": "Edit"           // Only Edit tool
"matcher": "Write|Edit"     // Either Write or Edit
"matcher": ".*"             // Any tool
```

## Professional Hook Examples

### 1. Auto-Format (Boris's Pattern)

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "bun run format || true"
    }]
  }]
}
```

**Why `|| true`**: Prevents hook failure from blocking Claude

### 2. Auto-Lint

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "eslint --fix . || true"
    }]
  }]
}
```

### 3. Auto-Format with Specific Tool

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "prettier --write . || true"
    }]
  }]
}
```

### 4. Auto-Type Check

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "tsc --noEmit || true"
    }]
  }]
}
```

**Note**: Type checking can be slow. Consider running only on specific files or before commit.

### 5. Run Tests After Changes

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "npm test -- --passWithNoTests || true"
    }]
  }]
}
```

### 6. Update Imports

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "organize-imports-cli || true"
    }]
  }]
}
```

### 7. Git Auto-Add

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "git add -A || true"
    }]
  }]
}
```

**Warning**: Use cautiously - auto-staging can be surprising

### 8. Multiple Hooks (Chained)

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [
      {
        "type": "command",
        "command": "prettier --write ."
      },
      {
        "type": "command",
        "command": "eslint --fix ."
      },
      {
        "type": "command",
        "command": "tsc --noEmit"
      }
    ]
  }]
}
```

**Note**: Hooks run sequentially in order

## File-Specific Hooks

Run different hooks based on file types:

```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "filePattern": "*.ts|*.tsx",
      "hooks": [{
        "type": "command",
        "command": "prettier --write ."
      }]
    },
    {
      "matcher": "Write|Edit",
      "filePattern": "*.py",
      "hooks": [{
        "type": "command",
        "command": "black ."
      }]
    }
  ]
}
```

## PrePromptSubmit Hooks

Run before sending messages to Claude.

### Use Case: Contextual Information

```json
{
  "PrePromptSubmit": [{
    "hooks": [{
      "type": "command",
      "command": "echo '\\n\\n[Current branch: $(git branch --show-current)]'"
    }]
  }]
}
```

Automatically includes current branch in context.

### Use Case: Environment Variables

```json
{
  "PrePromptSubmit": [{
    "hooks": [{
      "type": "command",
      "command": "export NODE_ENV=development"
    }]
  }]
}
```

## AgentStop Hooks

Run when background agents complete.

### Use Case: Notification

```json
{
  "AgentStop": [{
    "hooks": [{
      "type": "command",
      "command": "osascript -e 'display notification \"Agent completed\" with title \"Claude Code\"'"
    }]
  }]
}
```

**macOS**: Shows system notification when agent finishes

### Use Case: Verification

```json
{
  "AgentStop": [{
    "hooks": [{
      "type": "command",
      "command": "npm test && npm run build"
    }]
  }]
}
```

Automatically verify agent's work when it completes.

## Hook Best Practices

### 1. Always Use `|| true`

Prevents hook failures from blocking Claude:

```json
"command": "prettier --write . || true"
```

Without `|| true`, if prettier fails, Claude gets stuck.

### 2. Keep Hooks Fast

Slow hooks create friction:
- **Fast**: Prettier (~1s)
- **Medium**: ESLint (~3s)
- **Slow**: Full test suite (~30s)

For slow operations, use slash commands or manual triggers instead.

### 3. Make Hooks Idempotent

Hooks should be safe to run multiple times:
- **Good**: Format code (same result each time)
- **Bad**: Increment version number (changes each run)

### 4. Use Specific Matchers

Match only relevant tools:
```json
"matcher": "Write|Edit"  // Good - specific
"matcher": ".*"          // Bad - runs on everything
```

### 5. Silent by Default

Avoid noisy output:
```json
"command": "prettier --write . --log-level warn || true"
```

### 6. Team Consistency

Share hooks via `.claude/settings.json` in git:
```bash
git add .claude/settings.json
git commit -m "feat: add auto-format hooks"
```

## Advanced Patterns

### Conditional Hooks

Run hooks only in specific conditions:

```bash
# Only format if prettier config exists
"command": "[ -f .prettierrc ] && prettier --write . || true"
```

### Hooks with Context

Pass file path to hook:

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "echo 'Modified: $CLAUDE_FILE_PATH'"
    }]
  }]
}
```

**Note**: Check docs for available environment variables

### Incremental Hooks

Run only on changed files:

```bash
# Format only git-staged files
"command": "git diff --name-only --cached | xargs prettier --write || true"
```

## Common Hook Combinations

### JavaScript/TypeScript Project

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [
      {
        "type": "command",
        "command": "prettier --write . || true"
      },
      {
        "type": "command",
        "command": "eslint --fix . || true"
      }
    ]
  }]
}
```

### Python Project

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [
      {
        "type": "command",
        "command": "black . || true"
      },
      {
        "type": "command",
        "command": "isort . || true"
      },
      {
        "type": "command",
        "command": "flake8 . || true"
      }
    ]
  }]
}
```

### Rust Project

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "cargo fmt || true"
    }]
  }]
}
```

### Go Project

```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "gofmt -w . || true"
    }]
  }]
}
```

## Hooks vs Manual Commands

### Use Hooks For:
- Code formatting
- Linting
- Import organization
- Simple validations
- Fast operations (<3s)

### Use Slash Commands For:
- Running tests (can be slow)
- Building (can be slow)
- Complex workflows
- Operations requiring approval
- Debugging

### Use Manual Triggers For:
- Deployment
- Database migrations
- Destructive operations
- One-time tasks

## Debugging Hooks

### Problem: Hook not running

1. **Check syntax**: Valid JSON in settings
2. **Check matcher**: Pattern matches tool name
3. **Test command**: Run command manually first
4. **Check logs**: Claude Code shows hook execution

### Problem: Hook slowing down workflow

1. **Measure time**: How long does hook take?
2. **Optimize command**: Add filters, limit scope
3. **Consider removal**: Maybe manual is better

### Problem: Hook failing silently

1. **Remove `|| true`**: Temporarily to see errors
2. **Add logging**: Redirect output to file
3. **Test in isolation**: Run command outside Claude

```bash
# Debug hook
"command": "prettier --write . 2>&1 | tee /tmp/prettier.log || true"
```

## Hooks Configuration File

Complete example `.claude/settings.json`:

```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "command",
          "command": "prettier --write . || true",
          "description": "Auto-format code"
        },
        {
          "type": "command",
          "command": "eslint --fix . || true",
          "description": "Auto-fix linting issues"
        }
      ]
    }
  ],
  "AgentStop": [
    {
      "hooks": [{
        "type": "command",
        "command": "npm test",
        "description": "Run tests after agent completes"
      }]
    }
  ]
}
```

## Security Considerations

### Be Careful With:
- Hooks that delete files
- Hooks that make network requests
- Hooks that access secrets
- Hooks that modify git history

### Safe Practices:
- Review hook commands before adding
- Use read-only operations when possible
- Test hooks in safe environment first
- Document what each hook does

## Team Hook Guidelines

When sharing hooks with a team:

1. **Document purpose**: Comment each hook
2. **Make opt-in**: Use `.claude/settings.local.json` for personal hooks
3. **Test thoroughly**: Ensure hooks work on all systems
4. **Version tools**: Specify required tool versions
5. **Graceful degradation**: Use `|| true` for optional tools

## Hook Performance Tips

### Optimize Formatter

```bash
# Only format changed files
"command": "git diff --name-only | xargs prettier --write || true"
```

### Optimize Linter

```bash
# Lint only staged files
"command": "eslint --fix $(git diff --name-only --cached) || true"
```

### Parallel Execution

```bash
# Run hooks in parallel (bash)
"command": "(prettier --write . &); (eslint --fix . &); wait"
```

**Note**: Parallel execution is complex - use cautiously

## Next Steps

1. **Start simple**: Add auto-format hook
2. **Observe**: Does it improve workflow?
3. **Expand**: Add linting, type checking
4. **Optimize**: Remove slow hooks
5. **Share**: Check into git for team
6. **Combine**: Use with slash commands ([03-slash-commands.md](03-slash-commands.md))

## Resources

- [Claude Code Hooks Documentation](https://code.claude.com/docs/hooks)
- [Example Configurations](https://github.com/ChrisWiles/claude-code-showcase)
- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
