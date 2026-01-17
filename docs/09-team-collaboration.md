# Team Collaboration: Shared Knowledge & Workflows

## Boris's Team Approach

The Claude Code team at Anthropic embodies "Compounding Engineering" - collective learning that accumulates over time through shared configuration and knowledge.

**Key principle**: When Claude makes a mistake, add it to CLAUDE.md so the entire team benefits.

## The Team Knowledge Base

### Shared CLAUDE.md

**Single file checked into git**: Everyone contributes multiple times weekly.

**Example workflow**:
```
1. Developer works on feature
2. Claude makes mistake (e.g., uses wrong API pattern)
3. Developer fixes mistake
4. Developer updates CLAUDE.md: "Always use X pattern for APIs"
5. Team commits to git
6. All team members benefit immediately
```

**Result**: Team collectively learns, mistakes rarely repeat.

### Update Frequency

Boris's team: **Multiple times per week**

**When to update**:
- New pattern established
- Mistake discovered
- Tool/dependency changed
- Architecture decision made
- Common issue resolved

## Code Review Integration

### @.claude GitHub Action

Boris tags `@.claude` in PR comments to update CLAUDE.md automatically.

**Workflow**:
```
1. PR submitted
2. Reviewer notices pattern issue
3. Reviewer comments: "@.claude Always validate user input before processing"
4. GitHub Action updates CLAUDE.md
5. Pattern becomes permanent team knowledge
```

**Setup**: `.github/workflows/claude-md-update.yml`

```yaml
name: Update CLAUDE.md from Reviews

on:
  pull_request_review_comment:
    types: [created]

jobs:
  update-claude-md:
    if: contains(github.event.comment.body, '@.claude')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Extract suggestion
        run: |
          # Parse comment for suggestion
          # Update CLAUDE.md
          # Create commit
      - name: Push changes
        run: |
          git add CLAUDE.md
          git commit -m "docs: update CLAUDE.md from PR review"
          git push
```

### Manual PR Review Pattern

Even without automation:

```
Reviewer: "I notice you're using require() instead of import.
           Can you update CLAUDE.md to specify ES modules?"

Developer: [Updates CLAUDE.md]
           [Includes in PR]

Team: [Benefits from documentation]
```

## Shared Configuration Files

### What to Share

**Check into git**:
- `.claude/settings.json` - Team permissions
- `.claude/commands/` - Shared slash commands
- `.mcp.json` - External tool integrations
- `CLAUDE.md` - Project knowledge
- `.claude/agents/` - Custom subagents

**Add to .gitignore**:
- `.claude/settings.local.json` - Personal settings
- `.claude/CLAUDE.local.md` - Personal preferences
- `.mcp.json.local` - Personal MCP configs

### Example Shared Settings

**`.claude/settings.json`**:
```json
{
  "allowedPrompts": [
    "bun run build:*",
    "bun run test:*",
    "bun run typecheck:*",
    "git status",
    "git diff",
    "git log*"
  ],
  "PostToolUse": [{
    "matcher": "Write|Edit",
    "hooks": [{
      "type": "command",
      "command": "bun run format || true"
    }]
  }]
}
```

**Benefits**:
- Consistent permissions across team
- Same auto-formatting behavior
- Shared workflow automation

## Shared Slash Commands

### Team Command Library

**`.claude/commands/commit-push-pr.md`** (Boris's most-used):
```markdown
Create a commit and pull request following team conventions:

1. Run git status and git diff
2. Run git log to see recent commits
3. Stage relevant files
4. Create commit following our style (see CLAUDE.md)
5. Include co-author line
6. Push to remote
7. Create PR with proper template
```

Everyone on the team uses the same command.

### Building Team Commands

**Process**:
1. Individual discovers useful pattern
2. Creates command locally
3. Tests and refines
4. Shares with team
5. Team iterates and improves
6. Command becomes standard

**Result**: Collective automation library.

## Team CLAUDE.md Patterns

### Structure for Teams

```markdown
# Project Name

## Purpose
[What we're building and why]

## Tech Stack
[Technologies everyone should know]

## Team Conventions

### Code Style
- IMPORTANT: Always use ES modules (import/export)
- Use TypeScript strict mode
- Prefer functional components

### Git Workflow
- Branch naming: feature/*, bugfix/*, refactor/*
- Commit format: type(scope): description
- PR template: See .github/pull_request_template.md

### Testing
- IMPORTANT: Test coverage must stay above 80%
- Write tests before implementation (TDD)
- Use descriptive test names

### Architecture
- State management: Zustand (not Redux)
- API client: Fetch with retry logic
- Error handling: Centralized error boundary

## Verification
- IMPORTANT: Run `bun run typecheck` before committing
- Run `bun test` - all tests must pass
- Check browser console - 0 errors

## Documentation
- Architecture: docs/architecture.md
- API: docs/api/README.md
- Onboarding: docs/onboarding.md
```

### Rule: Only 30%+ Patterns

Boris's team only documents tools/APIs used by 30%+ of engineers.

**Why**: Keeps CLAUDE.md focused on universal patterns, not edge cases.

**Example**:
- ✅ "Use React Hook Form for all forms" (everyone uses)
- ❌ "Use lodash.debounce in the admin panel" (only one person)

## Onboarding New Team Members

### Day 1: Essential Reading

```markdown
# New Team Member Onboarding

## Read These First
1. CLAUDE.md (project conventions)
2. docs/architecture.md (system design)
3. docs/getting-started.md (setup)

## Setup Claude Code
1. Install: https://code.claude.com
2. Clone repo: git clone ...
3. Setup: bun install
4. Test: bun test
5. Verify: bun run typecheck

## Your First Task
Use /commit-push-pr to make a small documentation fix.
This will familiarize you with our workflow.
```

### Week 1: Learning Patterns

New member naturally learns from CLAUDE.md:
- Every session, Claude applies team conventions
- Mistakes are caught and explained
- Patterns become intuitive

**Result**: Faster onboarding than traditional documentation.

## Shared MCP Integration

### Team External Tools

**`.mcp.json`** (checked into git):
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    },
    "sentry": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
        "SENTRY_ORG": "team-org",
        "SENTRY_PROJECT": "main-project"
      }
    }
  }
}
```

Everyone gets access to the same tools.

**Personal tools** in `.mcp.json.local`:
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-notion"],
      "env": {
        "NOTION_TOKEN": "${MY_NOTION_TOKEN}"
      }
    }
  }
}
```

## Team Workflows

### Workflow 1: Compounding Engineering

```
Developer 1: Discovers pattern issue
           → Updates CLAUDE.md
           → Commits to git

Developer 2: Pulls latest
           → Claude applies new pattern
           → No repeat mistake

Developer 3: Works on similar feature
           → Automatically follows pattern
           → Higher quality from day 1
```

### Workflow 2: Pair Programming with Claude

```
Developer A: Works on backend
             Uses Session 1

Developer B: Works on frontend
             Uses Session 2

Both sessions reference same CLAUDE.md
→ Consistent patterns across full stack
```

### Workflow 3: Team Code Review

```
1. Developer creates PR
2. Claude Code GitHub Action runs checks
3. Reviewers use Claude to analyze PR
4. Reviewers tag @.claude with suggestions
5. CLAUDE.md updated automatically
6. Pattern available for future PRs
```

### Workflow 4: Incident Response

```
On-call engineer: Notices production error
Session 1: Investigates via Sentry MCP
Session 2: Reproduces locally
Session 3: Implements fix
Session 4: Creates PR with regression test
Session 5: Documents in CLAUDE.md

Next on-call: Reads CLAUDE.md, knows the pattern
```

## Team Anti-Patterns to Avoid

### ❌ Divergent CLAUDE.md Files

**Problem**: Team members maintain separate CLAUDE.md files
**Solution**: Single shared file, personal preferences in CLAUDE.local.md

### ❌ Outdated Documentation

**Problem**: CLAUDE.md not updated, becomes stale
**Solution**: Make updates part of PR requirements

### ❌ Personal Preferences as Team Rules

**Problem**: "I prefer tabs" added to shared CLAUDE.md
**Solution**: Defer to linter config, not CLAUDE.md

### ❌ No Review Process

**Problem**: Anyone can add anything to CLAUDE.md
**Solution**: Review CLAUDE.md changes in PRs like code

### ❌ Kitchen Sink Approach

**Problem**: CLAUDE.md grows to 1000+ lines
**Solution**: Keep under 300 lines, use progressive disclosure

## Team Metrics

Track team improvement:

### Before Shared Configuration
- New member productivity: 2-3 weeks to full speed
- Pattern consistency: 60%
- Repeated mistakes: Common
- Code review comments: 50% about style/patterns

### After Shared Configuration
- New member productivity: 3-5 days to full speed
- Pattern consistency: 95%
- Repeated mistakes: Rare
- Code review comments: 90% about logic/design

**Result**: 5-10x improvement in consistency and onboarding.

## Communication Patterns

### Async Collaboration

```
Developer 1: (Morning, US)
  Updates CLAUDE.md with API pattern
  Commits to git

Developer 2: (Evening, Europe)
  Pulls latest changes
  Claude automatically uses new pattern
  No synchronous communication needed
```

### Knowledge Sharing

```
Weekly team meeting:
1. Review CLAUDE.md changes from past week
2. Discuss why patterns were added
3. Refine or remove outdated patterns
4. Plan documentation improvements
```

### Slack Integration

```
#engineering channel:
Bot: "CLAUDE.md updated by @alice:
      'Always validate webhook signatures from Stripe'"

Team: Sees update in real-time
      Next PR automatically follows pattern
```

## Team Command Patterns

### Shared /commit-push-pr

Used dozens of times daily:
```markdown
1. Review changes (git status, git diff)
2. Stage files
3. Create commit with co-author
4. Push
5. Create PR with template
```

### Team-Specific Commands

Each team develops specialized commands:

**E-commerce team**:
- `/verify-checkout-flow` - Test payment processing
- `/analyze-cart-abandonment` - Query BigQuery
- `/deploy-to-staging` - Deployment workflow

**Internal tools team**:
- `/check-permissions` - Verify access control
- `/sync-with-main-app` - Keep tools in sync
- `/update-api-docs` - Generate documentation

## Scaling Team Configuration

### Small Team (2-5 people)

**Focus**:
- Single shared CLAUDE.md
- Basic shared commands
- Manual updates, simple workflows

### Medium Team (5-20 people)

**Add**:
- GitHub Action for automated updates
- More extensive command library
- MCP integration for shared tools
- Regular review meetings

### Large Team (20+ people)

**Add**:
- Monorepo with hierarchical CLAUDE.md
- Team-specific configuration
- Automated compliance checks
- Dedicated documentation maintainer

## Remote Team Considerations

### Time Zone Distribution

**Challenge**: Team spans US, Europe, Asia
**Solution**: Async updates via git, Slack bot notifications

### Language Differences

**Challenge**: Team speaks different languages
**Solution**: CLAUDE.md in English (standard), comments in native language OK

### Different Development Environments

**Challenge**: Mac, Linux, Windows users
**Solution**: OS-specific commands in settings.local.json, shared configs are cross-platform

## Team Security

### Shared Secrets Management

**Never in git**:
```json
❌ "SLACK_TOKEN": "xoxb-actual-token"
```

**Use environment variables**:
```json
✅ "SLACK_TOKEN": "${SLACK_BOT_TOKEN}"
```

**Team secret management**:
- 1Password shared vaults
- AWS Secrets Manager
- HashiCorp Vault

### Permission Boundaries

**Shared permissions** (safe for everyone):
```json
{
  "allowedPrompts": [
    "bun run test:*",
    "git status",
    "git diff"
  ]
}
```

**Restricted permissions** (require approval):
```
- Database writes
- Production deployments
- Secret access
```

## Measuring Team Success

### Key Indicators

1. **CLAUDE.md update frequency**: Multiple times per week
2. **Pattern consistency**: 90%+ in code reviews
3. **Onboarding time**: <1 week to productivity
4. **Repeated mistakes**: Near zero
5. **Code review efficiency**: 50% fewer style comments

### Team Retrospectives

Monthly review:
```
1. What patterns did we add to CLAUDE.md?
2. What mistakes did we prevent?
3. What automation did we build?
4. How did Claude Code improve our workflow?
5. What should we improve next month?
```

## Next Steps for Teams

### Week 1: Foundation
1. Create shared CLAUDE.md
2. Define basic conventions
3. Share with team

### Week 2: Automation
4. Add shared slash commands
5. Set up hooks
6. Configure permissions

### Week 3: Integration
7. Set up GitHub Action
8. Integrate MCP tools
9. Document workflows

### Week 4+: Optimization
10. Review and refine
11. Add advanced patterns
12. Scale to more team members

## Resources

- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- [Team Configuration Examples](https://github.com/ChrisWiles/claude-code-showcase)
- [Best Practices - Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
