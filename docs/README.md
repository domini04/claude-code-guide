# Claude Code Learning Blueprint

**Based on**: Boris Cherny's (Creator of Claude Code) professional setup and workflows - January 2026

## Overview

This documentation provides a comprehensive guide to mastering Claude Code, from basic concepts to advanced professional workflows. The structure follows a progressive learning path.

## Core Philosophy

> "Give Claude a way to verify its work - it will **2-3x the quality** of the final result."
> — Boris Cherny, Creator of Claude Code

### Key Principles
1. **Verification First**: Always create feedback loops
2. **Progressive Learning**: Master basics before advanced features
3. **Vanilla Over Custom**: Default settings work great; customize only when needed
4. **Shared Knowledge**: Team learning compounds through CLAUDE.md
5. **Parallel Execution**: Scale with multiple sessions, not single-session optimization

## Documentation Structure

### Foundation (Start Here)
- **[00-overview.md](00-overview.md)** - Claude Code fundamentals and Boris's setup
- **[01-claude-md-guide.md](01-claude-md-guide.md)** - Project knowledge base setup
- **[02-plan-mode-workflows.md](02-plan-mode-workflows.md)** - Plan before you code

### Essential Features
- **[03-slash-commands.md](03-slash-commands.md)** - Custom automations
- **[04-hooks-automation.md](04-hooks-automation.md)** - Automated formatting and checks
- **[05-permissions.md](05-permissions.md)** - Security and friction balance
- **[06-verification-quality.md](06-verification-quality.md)** - **THE MOST IMPORTANT** - Quality multiplier techniques

### Advanced Topics
- **[07-mcp-integration.md](07-mcp-integration.md)** - External tool integration (Slack, BigQuery, Sentry)
- **[08-parallel-sessions.md](08-parallel-sessions.md)** - Running multiple Claude instances
- **[09-team-collaboration.md](09-team-collaboration.md)** - Git workflows and shared patterns

## Learning Path

### Week 1: Foundation
1. Read 00-overview.md
2. Set up CLAUDE.md (01-claude-md-guide.md)
3. Practice Plan Mode (02-plan-mode-workflows.md)
4. Implement verification loops (06-verification-quality.md)

### Week 2: Automation
5. Create first slash command (03-slash-commands.md)
6. Set up PostToolUse hooks (04-hooks-automation.md)
7. Configure permissions (05-permissions.md)

### Week 3+: Advanced
8. Explore MCP integration (07-m cp-integration.md)
9. Try parallel sessions (08-parallel-sessions.md)
10. Implement team workflows (09-team-collaboration.md)

## Quick Reference

### Essential Commands
- **Shift+Tab (twice)**: Enter Plan Mode
- **`#` key**: Suggest CLAUDE.md additions
- **`/help`**: Get help with Claude Code
- **`/permissions`**: Manage allowed operations
- **`/init`**: Generate initial CLAUDE.md

### Boris's Most-Used Command
**`/commit-push-pr`**: Used dozens of times daily by the Claude Code team

### Model Recommendation
**Opus 4.5 with thinking mode**: Despite being slower, requires less steering and has better tool use - faster in the end.

## Success Metrics

You'll know you're succeeding when:
- [ ] Claude rarely makes the same mistake twice (CLAUDE.md working)
- [ ] You start sessions with Plan Mode habitually
- [ ] Every change has a verification step
- [ ] You've created at least 2-3 custom slash commands
- [ ] You're running multiple sessions for separate concerns

## Resources

### Official Documentation
- [Claude Code Docs](https://code.claude.com/docs)
- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

### Community Resources
- [How Boris Uses Claude Code](https://howborisusesclaudecode.com/)
- [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Claude Code Showcase (GitHub)](https://github.com/ChrisWiles/claude-code-showcase)

### Key Articles
- [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)
- [Cooking with Claude Code: The Complete Guide](https://www.siddharthbharath.com/claude-code-the-complete-guide/)
- [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)

## Contributing to This Documentation

As you learn:
1. Update CLAUDE.md with new patterns
2. Add learnings to relevant docs
3. Document mistakes and solutions
4. Share successful workflows

Remember: This is a living document. It should grow as you learn.
