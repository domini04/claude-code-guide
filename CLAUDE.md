# Claude Code Learning Project

## Purpose
Learning environment for mastering Claude Code features, based on Boris Cherny's professional workflows.

## Project Structure
```
/claude-code/
├── CLAUDE.md              # Project-wide instructions (you are here)
├── SESSION.md             # Current work tracking (gitignored)
├── docs/                  # Learning materials (00-09 guides)
│   └── README.md          # Start here for structured learning
├── practice-project/      # FastAPI app with intentional flaws
│   ├── CLAUDE.md          # Project-specific instructions
│   └── GUIDE.md           # Exercise walkthrough
└── .claude/
    ├── settings.local.json
    └── agents/            # Shared agents (code-reviewer, test-runner)
```

## Quick Start
- **New to Claude Code?** Start with `docs/README.md`
- **Hands-on practice?** See `practice-project/GUIDE.md`
- **Resuming work?** Check `SESSION.md`

## Learning Philosophy
1. Progressive disclosure - read docs on-demand, not upfront
2. Verification first - every change needs a way to verify
3. Plan before execute - use Plan Mode (Shift+Tab x2)

## Teaching Protocol
When demonstrating features for practice-project:
1. Introduce concept briefly
2. Show configuration location
3. Explain implications
4. **WAIT for "go" before executing**
5. Explain results after

NEVER rush through features. Understanding > completion speed.

## Documentation Index
| Topic | File | When to Read |
|-------|------|--------------|
| Learning path | `docs/README.md` | First time setup |
| CLAUDE.md mastery | `docs/01-claude-md-guide.md` | Setting up projects |
| Plan Mode | `docs/02-plan-mode-workflows.md` | Before complex tasks |
| Slash commands | `docs/03-slash-commands.md` | Creating automations |
| Hooks | `docs/04-hooks-automation.md` | Auto-formatting setup |
| Permissions | `docs/05-permissions.md` | Security configuration |
| Verification | `docs/06-verification-quality.md` | Quality improvement |
| MCP | `docs/07-mcp-integration.md` | External tool integration |
| Parallel sessions | `docs/08-parallel-sessions.md` | Scaling workflows |
| Team collaboration | `docs/09-team-collaboration.md` | Shared patterns |
| Plugins overview | `docs/10-plugins-guide.md` | Extending Claude Code |

## Session Continuity
- Update `SESSION.md` when starting/ending work sessions
- This file is gitignored (personal state)

## Constraints
- NEVER delete practice-project source files without backup
- NEVER skip verification steps when demonstrating features
