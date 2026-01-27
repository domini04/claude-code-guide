# Agent Council Tutorial

**Plugin**: `agent-council` from plugins-for-claude-natives
**Trigger**: "summon the council"
**Time**: ~15 minutes

## What You'll Learn

The agent-council plugin gathers perspectives from multiple AI models and synthesizes their viewpoints into a comprehensive analysis. Think of it as getting opinions from different experts in the same room.

## When to Use This

- Architectural decisions with long-term implications
- Controversial or debatable technical choices
- Strategic decisions (build vs buy, monolith vs microservices)
- When you want to challenge your own assumptions
- Complex trade-offs with no clear "right" answer

## The Problem: Single-Perspective Bias

Every AI model (and human) has biases:
- Claude might favor certain patterns
- Different models have different training data
- One perspective can miss important angles
- Confirmation bias is real

The council provides diverse viewpoints to counteract this.

---

## Exercise: Architecture Decision

### Scenario

Your startup is growing and you need to decide on architecture:

> "We have a successful monolithic Django app serving 50k users.
> We're planning features that will 10x our scale.
> Should we migrate to microservices now, or scale the monolith?"

This is exactly the kind of nuanced decision where multiple perspectives help.

### Step 1: Frame Your Question

Good council questions:
- Have legitimate arguments on multiple sides
- Involve trade-offs, not just facts
- Benefit from diverse perspectives

### Step 2: Summon the Council

Type naturally in Claude Code:

```
summon the council

Should we migrate our Django monolith to microservices now,
or continue scaling the monolith? We have 50k users,
planning for 500k, team of 5 developers.
```

### Step 3: Review the Perspectives

The council gathers and synthesizes opinions:

```markdown
## Council Deliberation: Monolith vs Microservices

### Perspectives Gathered

#### Pragmatist View
"Scale the monolith. Your team of 5 cannot effectively maintain
microservices. The operational overhead alone will slow you down.
Django can handle 500k users with proper caching and optimization.
Premature decomposition is a leading cause of startup failure."

#### Architect View
"Start extracting services strategically. Identify the 2-3 components
with different scaling characteristics. A gradual migration reduces
risk while building team expertise. Don't do a big-bang rewrite."

#### Operations View
"Consider your deployment capabilities first. Do you have container
orchestration? Service mesh? Distributed tracing? Without these,
microservices will create more problems than they solve."

#### Business View
"What's the cost of being wrong? If you migrate too early, you slow
down feature development. If you wait too long, you hit scaling walls.
At 50k→500k, you have time to optimize the monolith while preparing
for eventual decomposition."

### Synthesis

**Consensus**: Scale the monolith now, prepare for selective extraction.

**Recommended Approach**:
1. Invest in monolith optimization (caching, database, async tasks)
2. Identify natural service boundaries (but don't extract yet)
3. Build operational capabilities (containers, monitoring)
4. Extract first service only when you hit a specific bottleneck

**Key Insight**: The decision isn't binary. The real question is
"when and how to start decomposing" not "monolith or microservices."
```

---

## Understanding Council Output

| Section | What It Contains |
|---------|-----------------|
| Perspectives | Distinct viewpoints from different "experts" |
| Synthesis | Areas of agreement across perspectives |
| Recommended Approach | Actionable path forward |
| Key Insight | Often reframes the original question |

---

## Practice Scenarios

### 1. Build vs Buy
```
summon the council

Should we build our own authentication system or use Auth0/Clerk?
B2B SaaS, enterprise customers need SSO, team of 3, 6-month runway.
```

### 2. Technical Debt
```
summon the council

Our test coverage is 15%. Should we stop features and write tests,
or continue shipping and add tests incrementally?
Early-stage startup, product-market fit not yet confirmed.
```

### 3. Language/Stack Change
```
summon the council

Should we rewrite our Node.js backend in Go for better performance?
Current response times ~200ms, target is <50ms, team knows Node well.
```

---

## Tips for Best Results

1. **Provide rich context**: Team size, timeline, constraints
2. **Acknowledge trade-offs**: Show you understand both sides
3. **Ask strategic questions**: Tactical questions have clearer answers
4. **Be open to reframing**: The council often reveals better questions

## Council vs Tech Decision

| Use Case | Tool |
|----------|------|
| "A vs B" with clear evaluation criteria | `/dev:tech-decision` |
| Strategic decisions with multiple valid paths | "summon the council" |
| Factual comparison (features, benchmarks) | `/dev:tech-decision` |
| Nuanced trade-offs, long-term implications | "summon the council" |

---

## When NOT to Use

- Straightforward technical questions
- When you need to move fast (council takes time)
- When the answer depends on specific benchmarks (test instead)
- When you're the domain expert and just need validation

---

## Combining with Other Plugins

**Full decision workflow**:
1. `/clarify` → Define what you're deciding
2. `/dev:tech-decision` → Get factual comparison
3. "summon the council" → Get strategic perspectives
4. Make your decision with full context

---

## Next Steps

- Try the council on a real architectural decision you're facing
- Compare council synthesis with your initial intuition
- Move to [omc-modes-tutorial.md](omc-modes-tutorial.md) for autonomous execution
