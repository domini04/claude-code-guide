# Claude Code Overview

## What is Claude Code?

Claude Code is Anthropic's official CLI tool for AI-assisted software engineering. It provides an interactive terminal interface where Claude can read files, write code, execute commands, and help with complex development tasks.

## Why Claude Code?

Unlike chat interfaces, Claude Code can:
- **Access your codebase**: Read, search, and understand project structure
- **Execute commands**: Run tests, builds, git operations
- **Make changes**: Edit files with precise diffs
- **Verify work**: Test changes and iterate based on feedback
- **Remember context**: Use CLAUDE.md for persistent project knowledge

## Boris Cherny's Setup

Boris Cherny created Claude Code and leads the team at Anthropic. His setup represents battle-tested professional workflows.

### The Core Setup

**Parallel Sessions**: 5 terminal sessions + 5-10 web sessions (claude.ai/code)
- System notifications alert when input needed
- Separate git checkouts avoid conflicts
- Background (`&`) and `--teleport` commands for session management

**Model Choice**: Opus 4.5 with thinking mode (exclusively)
- Despite higher latency, requires less steering
- Better tool use and reasoning
- Faster end-to-end completion

**Team Knowledge**: Single CLAUDE.md checked into git
- Updated multiple times weekly
- Captures mistakes and preferences
- Team learns collectively

### Daily Workflow

1. **Start with Plan Mode**: Shift+Tab twice
2. **Refine approach**: Iterate on plan before execution
3. **Auto-accept mode**: Let Claude execute the approved plan
4. **Verification**: Tests, builds, browser checks
5. **Update CLAUDE.md**: Document learnings

### Most-Used Command
**`/commit-push-pr`**: Runs dozens of times daily
- Combines git operations
- Follows team conventions
- Includes verification steps

## The 2-3x Quality Multiplier

> "Give Claude a way to verify its work - it will 2-3x the quality of the final result."

This is THE most important insight. Verification closes the feedback loop:

- **Simple tasks**: Bash command output
- **Moderate complexity**: Test suite execution
- **Complex UI**: Browser/simulator testing
- **Domain-specific**: Custom verification for your context

## Key Features Overview

### 1. CLAUDE.md Files
**What**: Persistent context across all sessions
**Why**: Prevents repeating the same information
**How**: Create CLAUDE.md in project root, update as you learn

### 2. Plan Mode
**What**: Design before implementation
**How**: Shift+Tab twice to enter
**Why**: Refine approach, avoid wasted work

### 3. Slash Commands
**What**: Custom automations in `.claude/commands/`
**Why**: Codify repeated workflows
**Example**: `/commit-push-pr`, `/verify-app`

### 4. Hooks
**What**: Automated actions triggered by events
**Types**:
- PostToolUse: After Claude writes code
- PrePromptSubmit: Before sending messages
- AgentStop: When agents complete

**Example**: Auto-format after edits

### 5. Permissions
**What**: Control what Claude can execute
**Strategy**: Pre-allow safe commands vs. skipping all checks
**Example**: Allow `npm run test:*` but require approval for `rm -rf`

### 6. Subagents
**What**: Pre-built specialized agents
**Examples**:
- `code-simplifier`
- `verify-app`
- `build-validator`
- `code-architect`

### 7. MCP (Model Context Protocol) Integration
**What**: Connect external tools
**Examples**: Slack, BigQuery, Sentry, GitHub
**How**: Configure in `.mcp.json`

### 8. Background & Long-Running Tasks
**What**: Handle operations taking minutes/hours
**Methods**:
- Background agents with verification
- AgentStop hooks
- Ralph Wiggum plugin (autonomous loops)

## Philosophy: Vanilla Over Custom

Boris's setup is "surprisingly vanilla." Success comes from:
- **Disciplined fundamentals**: Plan Mode, verification
- **Parallel execution**: Multiple sessions, not optimization tricks
- **Shared learning**: Team knowledge compounds
- **Appropriate tools**: Use linters for style, not LLMs

Avoid over-customization. The defaults work great.

## Common Mistakes to Avoid

1. **Skipping Plan Mode**: Jumping straight to implementation
2. **No Verification**: Missing the 2-3x quality multiplier
3. **Overloading CLAUDE.md**: Too many instructions → Claude ignores them
4. **LLM for Linter's Job**: Use Prettier/ESLint, not Claude
5. **Single Session Tunnel Vision**: Scale with parallel sessions

## Success Indicators

You're using Claude Code well when:
- Starting with Plan Mode is habitual
- Every change has verification
- CLAUDE.md grows organically
- Mistakes rarely repeat
- Running multiple sessions for separate concerns

## Professional Workflows

### Code Review Integration
Tag `@.claude` in PR comments → GitHub Action updates CLAUDE.md
- Team learns from every review
- Patterns become permanent
- "Compounding Engineering"

### Error Handling
Sentry integration via MCP:
- Claude reads error logs
- Proposes fixes
- Verifies in staging

### Team Synchronization
- Shared `.claude/settings.json` for permissions
- Shared `.claude/commands/` for workflows
- Shared `.mcp.json` for tool integrations
- Shared CLAUDE.md for knowledge

## Getting Started Checklist

- [ ] Create initial CLAUDE.md
- [ ] Design a complex development task for model comparison
- [ ] Test Opus 4.5 vs Sonnet by comparing outputs
- [ ] Evaluate results using SOTA LLMs and manual review
- [ ] Practice Plan Mode (Shift+Tab twice)
- [ ] Add verification to first task
- [ ] Create first slash command
- [ ] Set up PostToolUse hook
- [ ] Configure permissions

## Next Steps

1. **Read**: [01-claude-md-guide.md](01-claude-md-guide.md) - Set up your knowledge base
2. **Practice**: [02-plan-mode-workflows.md](02-plan-mode-workflows.md) - Master planning
3. **Implement**: [06-verification-quality.md](06-verification-quality.md) - Add the quality multiplier

## Resources

- Official Docs: https://code.claude.com/docs
- Boris's Setup: https://howborisusesclaudecode.com/
- Best Practices: https://www.anthropic.com/engineering/claude-code-best-practices
