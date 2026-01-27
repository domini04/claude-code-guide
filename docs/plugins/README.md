# Plugin Tutorials Index

Interactive tutorials to master Claude Code plugins through hands-on exercises.

## Decision Tree: Which Plugin Should I Use?

```
START: What do you need?
│
├─► "I have a vague idea, need clear requirements"
│   └─► /clarify → [clarify-tutorial.md](clarify-tutorial.md)
│
├─► "I need to choose between technologies"
│   └─► /dev:tech-decision → [tech-decision-tutorial.md](tech-decision-tutorial.md)
│
├─► "I want multiple AI perspectives on a decision"
│   └─► "summon the council" → [agent-council-tutorial.md](agent-council-tutorial.md)
│
├─► "I want Claude to build something autonomously"
│   │
│   ├─► "Speed is priority (parallel execution)"
│   │   └─► ulw [task] → [omc-modes-tutorial.md](omc-modes-tutorial.md#ultrapilot)
│   │
│   ├─► "Budget is priority (cheaper tokens)"
│   │   └─► eco: [task] → [omc-modes-tutorial.md](omc-modes-tutorial.md#ecomode)
│   │
│   ├─► "Must complete with verification"
│   │   └─► ralph: [task] → [omc-modes-tutorial.md](omc-modes-tutorial.md#ralph)
│   │
│   └─► "Standard autonomous execution"
│       └─► autopilot: [task] → [omc-modes-tutorial.md](omc-modes-tutorial.md#autopilot)
│
└─► "I need coordinated multi-agent work"
    ├─► "Parallel agents on shared task list"
    │   └─► /swarm → [omc-modes-tutorial.md](omc-modes-tutorial.md#swarm)
    │
    └─► "Sequential stages with data passing"
        └─► /pipeline → [omc-modes-tutorial.md](omc-modes-tutorial.md#pipeline)
```

## Tutorials

### Requirements & Planning
| Tutorial | Plugin | Difficulty | Time |
|----------|--------|------------|------|
| [Clarify Tutorial](clarify-tutorial.md) | `/clarify` | Beginner | 10 min |
| [Tech Decision Tutorial](tech-decision-tutorial.md) | `/dev:tech-decision` | Beginner | 15 min |
| [Agent Council Tutorial](agent-council-tutorial.md) | agent-council | Intermediate | 15 min |

### Autonomous Execution
| Tutorial | Modes Covered | Difficulty | Time |
|----------|---------------|------------|------|
| [OMC Modes Tutorial](omc-modes-tutorial.md) | autopilot, eco, ralph, ulw, swarm, pipeline | Intermediate | 30 min |

## Skill Progression Path

### Level 1: Clarification (Start Here)
1. **[clarify-tutorial.md](clarify-tutorial.md)** - Learn to turn vague ideas into actionable specs
   - Prerequisite: None
   - Key skill: Structured requirement gathering

### Level 2: Decision Making
2. **[tech-decision-tutorial.md](tech-decision-tutorial.md)** - Make informed technology choices
   - Prerequisite: Understand your project needs
   - Key skill: Multi-source tech analysis

3. **[agent-council-tutorial.md](agent-council-tutorial.md)** - Get diverse AI perspectives
   - Prerequisite: Have a complex decision to make
   - Key skill: Synthesizing multiple viewpoints

### Level 3: Autonomous Execution
4. **[omc-modes-tutorial.md](omc-modes-tutorial.md)** - Master multi-agent orchestration
   - Prerequisite: Clear, well-defined tasks
   - Key skills: Choosing the right execution mode, parallel workflows

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                    PLUGINS QUICK REFERENCE                  │
├─────────────────────────────────────────────────────────────┤
│  CLARIFICATION                                              │
│    /clarify              Transform vague → precise          │
│                                                             │
│  DECISIONS                                                  │
│    /dev:tech-decision    Multi-source tech analysis         │
│    "summon the council"  Multi-AI perspective synthesis     │
│                                                             │
│  AUTONOMOUS EXECUTION (oh-my-claudecode)                    │
│    autopilot: [task]     Standard autonomous mode           │
│    eco: [task]           Budget-friendly (30-50% cheaper)   │
│    ralph: [task]         Persist until verified complete    │
│    ulw [task]            Parallel execution (3-5x faster)   │
│                                                             │
│  ORCHESTRATION                                              │
│    /swarm                Parallel agents, shared tasks      │
│    /pipeline             Sequential multi-stage work        │
│    /plan                 Planning interview first           │
└─────────────────────────────────────────────────────────────┘
```

## Before You Start

1. Ensure plugins are installed (see installation guides for each ecosystem)
2. Have a real or practice project to work with
3. Start with Level 1 tutorials before jumping to autonomous modes
