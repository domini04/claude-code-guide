# Claude Code Plugins Guide

## What Are Plugins?

Plugins extend Claude Code's capabilities beyond its built-in features. They add specialized workflows, multi-agent orchestration, and domain-specific tools that the core CLI doesn't provide.

**Native Claude Code** = Core features (Plan Mode, hooks, slash commands)
**Plugins** = Community-built extensions for advanced workflows

## When to Use Plugins vs Native Features

| Situation | Use This |
|-----------|----------|
| Simple file edits, refactoring | Native Claude Code |
| Need verification loops | Native (hooks + commands) |
| Vague requirements need clarification | Plugin: `/clarify` |
| Complex autonomous multi-file work | Plugin: oh-my-claudecode |
| Need multiple AI perspectives | Plugin: agent-council |
| Evaluating tech stack choices | Plugin: `/dev:tech-decision` |

## Plugin Ecosystems

### 1. plugins-for-claude-natives (team-attention)

Individual plugins for specific workflows:

| Plugin | Trigger | Best For |
|--------|---------|----------|
| **clarify** | `/clarify` | Turning vague ideas into precise specs |
| **agent-council** | "summon the council" | Getting diverse AI perspectives |
| **dev:tech-decision** | `/dev:tech-decision` | Library/framework/architecture decisions |
| **dev:dev-scan** | `/dev:dev-scan` | Developer community sentiment |
| **session-wrap** | `/session-wrap` | End-of-session documentation |
| **youtube-digest** | `/youtube-digest [url]` | Video research and summaries |

### 2. oh-my-claudecode (Yeachan-Heo)

Multi-agent orchestration with magic keywords:

| Mode | Keyword | Best For |
|------|---------|----------|
| **autopilot** | `autopilot:` | Full autonomous task execution |
| **ultrapilot** | `ulw` or `ultrapilot:` | Parallel work (3-5x faster) |
| **ecomode** | `eco:` | Budget-conscious work (30-50% cheaper) |
| **ralph** | `ralph:` | Persist until verified complete |
| **swarm** | `/swarm` | Coordinated parallel agents |
| **pipeline** | `/pipeline` | Sequential multi-stage workflows |
| **plan** | `/plan` | Planning interview before execution |

## Interactive Tutorials

Learn each plugin through hands-on exercises:

- **[Tutorial Index](plugins/README.md)** - Decision tree + all tutorials
- **[Clarify Tutorial](plugins/clarify-tutorial.md)** - Requirements refinement
- **[Tech Decision Tutorial](plugins/tech-decision-tutorial.md)** - Tech stack analysis
- **[Agent Council Tutorial](plugins/agent-council-tutorial.md)** - Multi-AI perspectives
- **[OMC Modes Tutorial](plugins/omc-modes-tutorial.md)** - oh-my-claudecode deep dive

## Quick Decision Guide

```
Need to clarify vague requirements?     → /clarify
Making a technology choice?             → /dev:tech-decision
Want multiple AI perspectives?          → "summon the council"
Autonomous feature implementation?      → autopilot: [task]
Need it faster (parallel execution)?    → ulw [task]
Budget-conscious work?                  → eco: [task]
Must complete with verification?        → ralph: [task]
```

## Next Steps

1. Start with the [Tutorial Index](plugins/README.md) to find your first plugin
2. Try `/clarify` on your next vague requirement
3. Experiment with `autopilot:` on a small, isolated task
