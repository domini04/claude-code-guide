# Tech Decision Tutorial

**Plugin**: `dev:tech-decision` from plugins-for-claude-natives
**Trigger**: `/dev:tech-decision`
**Time**: ~15 minutes

## What You'll Learn

The `/dev:tech-decision` plugin provides structured analysis for technology choices by researching multiple sources and synthesizing recommendations.

## When to Use This

- Choosing between libraries (React vs Vue vs Svelte)
- Database selection (PostgreSQL vs MongoDB vs SQLite)
- Architecture decisions (monolith vs microservices)
- Framework evaluation (FastAPI vs Django vs Flask)
- Any "A vs B" technology comparison

## The Problem: Information Overload

Technology decisions are hard because:
- Documentation is biased toward each option
- Blog posts are often outdated or superficial
- Your specific context matters
- Trade-offs aren't always clear

---

## Exercise: Database Selection

### Scenario

You're building a new web application and need to choose a database. Your requirements:
- Expected 10,000 users initially
- Read-heavy workload (90% reads)
- Need full-text search
- Single server deployment to start
- Team is familiar with SQL

### Step 1: Frame Your Question

A good tech decision question includes context:

```
Should I use SQLite or PostgreSQL for a web app with 10k users,
read-heavy workload, needing full-text search, starting on a single server?
```

### Step 2: Run the Plugin

```
/dev:tech-decision
```

Provide your question when prompted.

### Step 3: Review the Analysis

The plugin researches and produces structured output:

```markdown
## Tech Decision: SQLite vs PostgreSQL

### Context Summary
- Scale: 10k users (small-medium)
- Workload: 90% reads
- Features needed: Full-text search
- Deployment: Single server
- Team skills: SQL familiar

### Option Analysis

#### SQLite
**Pros**:
- Zero configuration, embedded
- Excellent read performance
- Simpler deployment and backup
- Lower operational overhead

**Cons**:
- Write concurrency limitations
- Full-text search (FTS5) less mature than PostgreSQL
- Harder to migrate away later
- No built-in replication

#### PostgreSQL
**Pros**:
- Battle-tested full-text search
- Scales beyond single server when needed
- Rich ecosystem (extensions, tools)
- Better write concurrency

**Cons**:
- Requires separate service
- More operational complexity
- Overkill for current scale

### Recommendation
**PostgreSQL** - The full-text search requirement tips the balance.
While SQLite could work, PostgreSQL's mature FTS and growth path
make it the safer choice. Operational overhead is manageable with
modern tooling (Docker, managed services).

### Sources Consulted
- PostgreSQL vs SQLite benchmark comparisons
- Full-text search capability analysis
- Community discussions on scaling patterns
```

---

## Understanding the Output

The plugin provides:

| Section | Purpose |
|---------|---------|
| Context Summary | Confirms understanding of your needs |
| Option Analysis | Objective pros/cons for each choice |
| Recommendation | Synthesized suggestion with reasoning |
| Sources | Transparency on research performed |

---

## Practice Scenarios

Try these tech decisions:

### 1. Frontend Framework (Beginner)
```
React or Vue for a small team building an internal dashboard?
Team has no prior experience with either.
```

### 2. API Architecture (Intermediate)
```
REST vs GraphQL for a mobile app backend?
Multiple client types (iOS, Android, Web), frequent schema changes expected.
```

### 3. Caching Strategy (Advanced)
```
Redis vs in-memory caching for a Python web app?
Need session storage and rate limiting, running on Kubernetes.
```

---

## Tips for Best Results

1. **Provide context**: Team size, scale, constraints
2. **Be specific**: "Database for X" beats "which database?"
3. **Mention constraints**: Budget, timeline, team skills
4. **List must-haves**: Features you can't compromise on

## What This Plugin Isn't

- Not a replacement for prototyping (still validate your choice)
- Not always current (technology moves fast)
- Not a substitute for domain expertise (you know your context best)

---

## Combining with Other Plugins

**Clarify + Tech Decision workflow**:
1. `/clarify` → Define what you're building
2. `/dev:tech-decision` → Choose the right tools
3. `autopilot:` → Build it

---

## Next Steps

- Run a tech decision for your current project
- Compare the recommendation with your intuition
- Move to [agent-council-tutorial.md](agent-council-tutorial.md) for complex decisions needing multiple perspectives
