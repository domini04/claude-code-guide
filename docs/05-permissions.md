# Permissions Strategy

## What Are Permissions?

Permissions control what Claude Code can execute without manual approval. They balance security (preventing dangerous operations) with productivity (reducing friction).

## Boris's Approach

Boris DOES NOT use `--dangerously-skip-permissions`. Instead, he pre-allows safe commands via `/permissions`.

**Team-shared permissions** in `.claude/settings.json`:
```json
{
  "allowedPrompts": [
    "bun run build:*",
    "bun run test:*",
    "bun run typecheck:*"
  ]
}
```

**Result**: Safe commands auto-approved, dangerous ones still require confirmation.

## Permission Models

### 1. Default (Recommended)
**Behavior**: Claude asks before executing any bash command
**Pros**: Maximum safety
**Cons**: Some friction
**Best for**: Most users, production environments

### 2. Pre-Allowed Commands (Boris's Pattern)
**Behavior**: Whitelist safe commands, ask for everything else
**Pros**: Balance of safety and productivity
**Cons**: Requires setup
**Best for**: Professional workflows, teams

### 3. Skip All Permissions (Not Recommended)
**Behavior**: `--dangerously-skip-permissions` flag
**Pros**: Zero friction
**Cons**: Claude can execute ANY command
**Best for**: Sandboxed environments only

## Setting Up Pre-Allowed Commands

### Via `/permissions` Command

```
User: /permissions
Claude: [Shows permission management UI]
```

Add patterns for safe commands:
- `npm run test:*`
- `npm run build:*`
- `npm run lint:*`
- `git status`
- `git diff`
- `git log`

### Via Settings File

Create/edit `.claude/settings.json`:

```json
{
  "allowedPrompts": [
    "npm run test:*",
    "npm run build:*",
    "npm run lint:*",
    "git status",
    "git diff",
    "git log*"
  ]
}
```

### Via Settings.local.json

For personal-only permissions:

```json
{
  "allowedPrompts": [
    "open -a 'Google Chrome' http://localhost:3000"
  ]
}
```

Add to `.gitignore`:
```
.claude/settings.local.json
```

## Permission Patterns

### Wildcard Matching

```json
{
  "allowedPrompts": [
    "npm run test:*",      // Matches: npm run test:unit, npm run test:e2e
    "git log*",            // Matches: git log, git log --oneline
    "docker ps*"           // Matches: docker ps, docker ps -a
  ]
}
```

### Exact Matching

```json
{
  "allowedPrompts": [
    "git status",          // Exact match only
    "npm test",            // Exact match only
    "pwd"                  // Exact match only
  ]
}
```

## Safe Commands to Pre-Allow

### Read-Only Git Commands

```json
{
  "allowedPrompts": [
    "git status",
    "git diff",
    "git diff --cached",
    "git log*",
    "git show*",
    "git branch",
    "git remote -v"
  ]
}
```

### Build & Test Commands

```json
{
  "allowedPrompts": [
    "npm run build:*",
    "npm run test:*",
    "npm run lint:*",
    "npm run typecheck:*",
    "npm run format:*"
  ]
}
```

### Development Servers

```json
{
  "allowedPrompts": [
    "npm run dev",
    "npm start",
    "python manage.py runserver",
    "cargo run"
  ]
}
```

### Information Commands

```json
{
  "allowedPrompts": [
    "pwd",
    "ls*",
    "cat*",
    "head*",
    "tail*",
    "wc*",
    "find*",
    "grep*"
  ]
}
```

**Note**: Claude Code has dedicated tools (Read, Grep, Glob) that don't require bash permissions.

## Commands to NEVER Pre-Allow

### Destructive Operations

```json
❌ "rm -rf*"
❌ "git reset --hard*"
❌ "git push --force*"
❌ "drop database*"
❌ "truncate table*"
```

### Write Operations

```json
❌ "git push*"           // Require manual approval
❌ "git commit*"         // Should review commit messages
❌ "npm publish*"        // Dangerous for packages
❌ "docker rm*"          // Could remove important containers
```

### System Commands

```json
❌ "sudo*"               // System-level changes
❌ "chmod*"              // Permission changes
❌ "chown*"              // Ownership changes
❌ "mv*"                 // File moves (use with caution)
```

### Network Commands

```json
❌ "curl -X POST*"       // Could make changes
❌ "curl -X DELETE*"     // Destructive API calls
❌ "wget*"               // Could download malicious files
```

## Permission Strategy by Project Type

### Frontend Project

```json
{
  "allowedPrompts": [
    "npm run dev",
    "npm run build:*",
    "npm run test:*",
    "npm run lint:*",
    "npm run typecheck",
    "git status",
    "git diff",
    "git log*"
  ]
}
```

### Backend API

```json
{
  "allowedPrompts": [
    "npm run dev",
    "npm run test:*",
    "npm run db:migrate",       // Safe if read-only
    "git status",
    "git diff",
    "git log*",
    "docker ps",                // Read-only
    "docker logs*"              // Read-only
  ]
}
```

### Full-Stack Monorepo

```json
{
  "allowedPrompts": [
    "pnpm run dev",
    "pnpm run build:*",
    "pnpm run test:*",
    "pnpm run lint:*",
    "pnpm run typecheck",
    "turbo run*",
    "git status",
    "git diff",
    "git log*"
  ]
}
```

### Python Project

```json
{
  "allowedPrompts": [
    "python manage.py runserver",
    "python manage.py test*",
    "pytest*",
    "python -m unittest*",
    "black --check*",
    "mypy*",
    "git status",
    "git diff",
    "git log*"
  ]
}
```

## Dynamic Permissions

Allow permissions during execution:

```
User: Add authentication feature
Claude: This requires running `npm install jsonwebtoken`.
        Can I run: npm install jsonwebtoken?

User: [Approves]
Claude: [Executes and continues]
```

You can say "yes to all" for current session.

## Team Permission Strategy

### Shared Permissions (.claude/settings.json)

```json
{
  "allowedPrompts": [
    "npm run test:*",
    "npm run build:*",
    "git status",
    "git diff"
  ]
}
```

Check into git:
```bash
git add .claude/settings.json
git commit -m "feat: add team permissions"
```

### Personal Permissions (.claude/settings.local.json)

```json
{
  "allowedPrompts": [
    "open -a 'Google Chrome' http://localhost:3000",
    "code ."
  ]
}
```

Add to `.gitignore`:
```
.claude/settings.local.json
```

## Audit Trail

Track what Claude executes:

### Enable Command Logging

Add to settings:
```json
{
  "logCommands": true,
  "logFile": ".claude/command-log.txt"
}
```

### Review Logs

```bash
tail -f .claude/command-log.txt
```

Add to `.gitignore`:
```
.claude/command-log.txt
```

## Permission Scopes

### Session Scope
Granted for current session only:
```
User: [Approves npm install during conversation]
```
Next session requires approval again.

### Permanent Scope
Granted via settings file:
```json
{
  "allowedPrompts": ["npm install*"]
}
```
Always allowed in all sessions.

## Handling Permission Prompts

### When Claude Asks Permission

```
Claude: I need to run: npm install lodash
        This requires permission. Approve?
```

**Options**:
1. **Approve once**: For this command only
2. **Approve for session**: For all similar commands this session
3. **Add to allowedPrompts**: Permanent approval
4. **Deny**: Don't run the command

### Best Response Pattern

```
User: Yes, and add "npm install*" to allowedPrompts
```

Claude updates settings file and executes.

## Security Best Practices

### 1. Principle of Least Privilege

Only allow what's necessary:
```json
// Good
"npm run test:unit"

// Bad (too broad)
"npm*"
```

### 2. Read-Only When Possible

Prefer commands that don't modify state:
```json
// Safe
"git status"
"git diff"
"docker ps"

// Requires approval
"git commit"
"git push"
"docker rm"
```

### 3. Separate Production and Development

Development:
```json
{
  "allowedPrompts": [
    "npm run dev",
    "npm run test:*"
  ]
}
```

Production:
```json
{
  "allowedPrompts": [
    "npm run build",
    "npm run test:unit"
  ]
}
```

### 4. Review Settings Regularly

```bash
# Check what's allowed
cat .claude/settings.json

# Remove unused permissions
```

### 5. Use `.gitignore` for Sensitive Permissions

```
.claude/settings.local.json
.claude/secrets.json
```

## Common Permission Mistakes

### ❌ Allowing Everything

```json
{
  "allowedPrompts": ["*"]  // DON'T DO THIS
}
```

Equivalent to `--dangerously-skip-permissions`.

### ❌ Allowing Dangerous Patterns

```json
{
  "allowedPrompts": [
    "rm*",           // Could delete everything
    "git push*",     // Could force push
    "sudo*"          // System access
  ]
}
```

### ❌ Not Using Wildcards Properly

```json
{
  "allowedPrompts": [
    "npm run test"   // Only exact match
  ]
}
```

Should be:
```json
{
  "allowedPrompts": [
    "npm run test:*"  // Matches all test commands
  ]
}
```

### ❌ Mixing Personal and Team Settings

Personal preferences in shared settings file:
```json
// In .claude/settings.json (checked into git)
{
  "allowedPrompts": [
    "open -a 'Safari' *"  // Mac-specific, personal
  ]
}
```

Should be in `.claude/settings.local.json`.

## Troubleshooting

### Problem: Permission denied for safe command

**Solution**: Add to allowedPrompts
```json
{
  "allowedPrompts": ["npm run test:*"]
}
```

### Problem: Too many permission prompts

**Solution**: Review common commands, add patterns
```
# Track common commands
User: What commands am I approving frequently?
Claude: [Analyzes recent prompts]
User: Add the top 5 to allowedPrompts
```

### Problem: Accidentally allowed dangerous command

**Solution**: Remove from settings immediately
```bash
# Edit settings
code .claude/settings.json
# Remove the dangerous pattern
# Restart Claude Code
```

### Problem: Team member added unsafe permission

**Solution**: Code review settings changes
```bash
git diff .claude/settings.json
# Review permissions before merging
```

## Next Steps

1. **Review current permissions**: Run `/permissions`
2. **Identify safe commands**: What do you run repeatedly?
3. **Add to settings**: Create `.claude/settings.json`
4. **Test**: Verify commands auto-approve
5. **Share with team**: Check into git
6. **Combine with hooks**: See [04-hooks-automation.md](04-hooks-automation.md)

## Resources

- [Claude Code Permissions Documentation](https://code.claude.com/docs/permissions)
- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
