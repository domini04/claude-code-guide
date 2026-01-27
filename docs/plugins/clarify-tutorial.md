# Clarify Plugin Tutorial

**Plugin**: `clarify` from plugins-for-claude-natives
**Trigger**: `/clarify`
**Time**: ~10 minutes

## What You'll Learn

The `/clarify` plugin transforms vague, ambiguous requirements into precise, actionable specifications through a structured interview process.

## When to Use This

- Starting a new feature with unclear scope
- User stories that lack specifics
- "Build me a thing" requests
- Any task where you'd normally ask 5+ clarifying questions

## The Problem: Vague Requirements

Consider this common scenario:

> "Build a user dashboard"

What's wrong with this?
- What data should it show?
- Who are the users?
- What actions can users take?
- What's the layout?
- Are there permissions involved?

Without clarification, you'll either build the wrong thing or waste time iterating.

---

## Exercise: Transform Vague to Precise

### Step 1: Start with a Vague Requirement

Copy this intentionally vague requirement:

```
Build a user dashboard for our application
```

### Step 2: Run the Clarify Plugin

Type in Claude Code:

```
/clarify
```

Then provide your vague requirement when prompted.

### Step 3: Answer the Interview Questions

The plugin will ask targeted questions like:
- What is the primary purpose of this dashboard?
- Who will use it (roles/personas)?
- What key metrics or data should be displayed?
- What actions should users be able to take?
- What's the priority order of features?

**Tip**: Answer honestly, even if you're unsure. The plugin helps surface what you *don't* know.

### Step 4: Review the Output

The plugin produces a structured specification like:

```markdown
## Clarified Requirements: User Dashboard

### Purpose
Real-time overview of user activity and account health

### Target Users
- End users (view own data)
- Support staff (view any user, read-only)

### Core Features (Priority Order)
1. Activity timeline (last 30 days)
2. Account health score with breakdown
3. Quick actions: password reset, notification settings
4. Support ticket history

### Data Requirements
- User activity logs (API calls, logins)
- Account metrics (storage, API usage)
- Support ticket status

### Constraints
- Mobile-responsive design
- Load time < 2 seconds
- No PII visible to support staff
```

---

## Before/After Comparison

| Aspect | Before (Vague) | After (Clarified) |
|--------|----------------|-------------------|
| Scope | "user dashboard" | 4 specific features prioritized |
| Users | Unknown | End users + support staff |
| Data | Unknown | Activity, metrics, tickets |
| Constraints | None stated | Mobile, performance, privacy |
| Actionable? | No | Yes |

---

## Practice Scenarios

Try `/clarify` with these vague requirements:

1. **Easy**: "Add search to the app"
2. **Medium**: "We need better error handling"
3. **Hard**: "Make the app faster"

Each will reveal different clarification needs.

---

## Tips for Best Results

1. **Be honest about unknowns**: "I'm not sure" is a valid answer
2. **Think about edge cases**: The interview often reveals them
3. **Capture stakeholder input**: Run clarify with stakeholders present
4. **Save the output**: Use it as your requirements doc

## When NOT to Use

- Requirements are already crystal clear
- Simple, obvious tasks ("fix this typo")
- You're the domain expert and know exactly what's needed

---

## Next Steps

- Try `/clarify` on a real project requirement
- Compare results with what you would have built without clarification
- Move to [tech-decision-tutorial.md](tech-decision-tutorial.md) for technology choices
