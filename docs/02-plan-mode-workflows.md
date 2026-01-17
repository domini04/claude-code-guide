# Plan Mode & Workflows

## What is Plan Mode?

Plan Mode is Claude Code's planning interface where you design an implementation approach before Claude executes changes. It's the foundation of professional Claude Code workflows.

**Key insight**: "Measure twice, cut once" - applied to AI coding.

## Why Plan Mode Matters

### Without Plan Mode
1. User: "Add authentication"
2. Claude: *Immediately starts writing code*
3. User: "Wait, I wanted OAuth, not JWT"
4. Result: Wasted time, code to undo

### With Plan Mode
1. User: "Add authentication"
2. Claude: *Enters Plan Mode, proposes approach*
3. User: Reviews plan, clarifies "Use OAuth with Google"
4. Claude: *Executes refined plan correctly*
5. Result: Right solution, first try

## How to Enter Plan Mode

**Keyboard shortcut**: `Shift+Tab` (press twice)

**Result**: Claude enters planning mode where it will:
1. Explore the codebase
2. Design an implementation approach
3. Present a plan for your approval
4. Wait for your confirmation before executing

## Boris's Plan Mode Workflow

Boris Cherny starts most sessions in Plan Mode:

1. **Enter Plan Mode**: Shift+Tab twice
2. **Iterate on Plan**: Refine approach with Claude
3. **Approve**: Once plan is solid
4. **Auto-Accept Mode**: Claude executes without interruption
5. **Typically completes in one pass**

This is his default workflow, not an exception.

## The Plan Mode Process

### Phase 1: Exploration
Claude investigates your codebase:
- Searches for relevant files
- Reads existing code
- Understands patterns and architecture
- Identifies dependencies

### Phase 2: Design
Claude proposes an approach:
- Step-by-step implementation plan
- Files to create/modify
- Potential risks or considerations
- Alternative approaches (if applicable)

### Phase 3: Refinement
You provide feedback:
- Ask questions
- Clarify requirements
- Suggest alternatives
- Request more detail

### Phase 4: Approval
When satisfied, approve the plan:
- Claude exits Plan Mode
- Begins execution
- Follows the approved approach

## When to Use Plan Mode

### Always Use For:
- **New features**: Any meaningful new functionality
- **Multiple-file changes**: Affects 3+ files
- **Architecture decisions**: Choosing patterns or technologies
- **Refactoring**: Restructuring existing code
- **Unclear scope**: Need to explore before understanding

### Rarely Use For:
- **Obvious fixes**: Single-line typos
- **Tiny changes**: Adding a console.log
- **Explicit instructions**: User provided detailed steps

### The 80/20 Rule
If uncertain, use Plan Mode. Better to plan unnecessarily than fix mistakes later.

## Plan Mode Best Practices

### 1. Give Context First
**Good**:
```
User: I want to add user authentication. We're building a SaaS app
that needs to support both email/password and Google OAuth. Security
is important. What approach do you recommend?

[Shift+Tab twice to enter Plan Mode]
```

**Less Effective**:
```
User: Add authentication
[Enters Plan Mode but Claude lacks context]
```

### 2. Iterate on the Plan
Don't accept the first plan if you have concerns.

```
Claude: [Proposes JWT-based auth]
User: I'm concerned about token storage. What about refresh token rotation?
Claude: [Updates plan with refresh token strategy]
User: Looks good, proceed
```

### 3. Ask for Alternatives
```
User: Show me 2-3 different approaches with trade-offs
Claude:
  Option 1: JWT - Simple, stateless, scales easily
  Option 2: Session-based - More secure, requires Redis
  Option 3: OAuth only - Outsource to providers
```

### 4. Request Verification Steps
```
User: Include verification steps in the plan
Claude: [Plan now includes: "Test with curl, run integration tests, verify in browser"]
```

### 5. Use Plan Mode for Research
Even if not implementing, Plan Mode helps understand codebases:

```
User: I'm trying to understand how error handling works in this codebase.
Can you explore and explain the patterns?

[Shift+Tab twice]
Claude: [Explores, finds patterns, documents findings]
```

## Auto-Accept Workflow

After approving a plan, switch to auto-accept mode for uninterrupted execution.

### How to Enable Auto-Accept
```bash
claude --auto-accept
```

Or configure in settings:
```json
{
  "autoAcceptEdits": true
}
```

### Boris's Pattern
1. Plan Mode: Refine approach
2. Approve plan
3. Auto-accept: Claude executes without prompts
4. Typically completes in one pass

### When NOT to Auto-Accept
- First time trying a complex operation
- Working with production systems
- Unsure about Claude's approach
- Learning Claude Code (you want to see each step)

## Plan Mode Permissions

During Plan Mode, you can pre-approve certain actions:

```
Claude: This plan requires:
- Running npm install
- Running npm test
- Creating 3 new files
- Modifying 5 existing files

Approve these permissions for the plan?
```

This reduces friction during execution.

## Common Plan Mode Scenarios

### Scenario 1: New Feature
```
User: Add a dark mode toggle to the app settings
[Shift+Tab twice]

Claude explores and proposes:
1. Add theme context provider
2. Create toggle component
3. Update color scheme
4. Persist preference to localStorage
5. Add toggle to settings page

User: Can we use system preference as default?
Claude: [Updates plan to check prefers-color-scheme]
User: Perfect, proceed
```

### Scenario 2: Bug Investigation
```
User: Users report the checkout form crashes. Investigate and fix.
[Shift+Tab twice]

Claude explores:
1. Reads checkout form component
2. Checks error logs
3. Identifies null pointer in payment validation
4. Proposes fix with defensive checks
5. Suggests adding error boundary

User: Add the error boundary but also add validation tests
Claude: [Updates plan with test requirements]
User: Approved
```

### Scenario 3: Refactoring
```
User: This component is 800 lines. Help me refactor it.
[Shift+Tab twice]

Claude explores and proposes:
1. Extract form logic to custom hook
2. Split into 4 smaller components
3. Move API calls to service layer
4. Update tests

User: Keep the component structure but focus on extracting the hook
Claude: [Revises plan to focus on hook extraction]
User: That's better, go ahead
```

### Scenario 4: Architecture Decision
```
User: We need to add real-time notifications. What's the best approach?
[Shift+Tab twice]

Claude investigates current architecture and proposes:
Option 1: WebSockets (Socket.io)
  Pros: Full duplex, mature
  Cons: Requires separate server, complex deployment

Option 2: Server-Sent Events (SSE)
  Pros: Simple, HTTP-based, works with existing server
  Cons: One-way only

Option 3: Polling
  Pros: Simplest implementation
  Cons: Inefficient, higher latency

Recommendation: SSE given your existing Express setup

User: Let's go with SSE
Claude: [Proceeds with SSE implementation]
```

## Combining Plan Mode with Verification

The most powerful workflow combines planning with verification:

```
User: Add a search feature with autocomplete
[Shift+Tab twice]

Claude proposes plan:
1. Create search API endpoint
2. Add debounced search input
3. Display results with highlighting
4. Add keyboard navigation
5. VERIFICATION:
   - Unit tests for API endpoint
   - Integration test for search flow
   - Manual test: Type "react" and verify results
   - Check keyboard navigation (arrow keys, enter)

User: Approved
Claude: [Implements and verifies each step]
```

## Plan Mode Alternatives

### Without Entering Plan Mode Explicitly
You can get planning behavior without the formal mode:

```
User: Before you implement this, explain your approach and get my approval
Claude: [Proposes approach, waits for approval]
```

But formal Plan Mode is clearer and more reliable.

## Advanced: Multi-Session Planning

For large projects, use Plan Mode in one session to create the plan, then execute in another:

**Session 1 (Planning)**:
```
User: I need to migrate from REST to GraphQL. Create a migration plan.
[Shift+Tab twice]
Claude: [Creates comprehensive plan, saves to MIGRATION_PLAN.md]
```

**Session 2+ (Execution)**:
```
User: Follow MIGRATION_PLAN.md - start with step 1
Claude: [Executes step 1]
User: Next step
Claude: [Executes step 2]
...
```

## Plan Mode + Parallel Sessions

Boris runs 5 sessions in parallel. Plan Mode helps coordinate:

**Session 1**: Plan backend API changes
**Session 2**: Plan frontend updates
**Session 3**: Plan database migrations
**Session 4**: Plan test updates
**Session 5**: Integration review

Each session plans independently, then executes in coordinated order.

## Troubleshooting Plan Mode

### Problem: Claude starts coding without planning
**Solution**: Explicitly enter Plan Mode with Shift+Tab twice

### Problem: Plan is too vague
**Solution**: Ask for more detail
```
User: Can you break down step 3 into sub-steps?
User: What specific files will you modify?
User: Show me the proposed API interface
```

### Problem: Plan doesn't match my needs
**Solution**: Iterate, don't accept
```
User: I prefer a different approach - let me describe it...
User: Can you revise the plan to use X instead of Y?
```

### Problem: Too many iterations
**Solution**: Provide more context upfront
- Explain constraints
- Share preferences
- Reference similar code
- Be specific about requirements

## Measuring Success

You're using Plan Mode well when:
- [ ] Starting sessions with Plan Mode is habitual
- [ ] Rework is rare (right the first time)
- [ ] You catch issues before execution
- [ ] Estimates are accurate (plan reflects reality)
- [ ] Less time explaining "that's not what I wanted"

## Quick Reference

| Action | Command |
|--------|---------|
| Enter Plan Mode | `Shift+Tab` (twice) |
| Exit Plan Mode (approve) | Say "approved" or "proceed" |
| Revise plan | Provide feedback, ask questions |
| Cancel Plan Mode | Say "cancel" or "never mind" |
| Auto-accept after plan | Enable in settings or use flag |

## Next Steps

1. **Practice**: Try Plan Mode on your next feature
2. **Observe**: Notice the difference in quality
3. **Iterate**: Refine your planning prompts
4. **Combine**: Use with verification (see [06-verification-quality.md](06-verification-quality.md))
5. **Scale**: Apply to parallel sessions (see [08-parallel-sessions.md](08-parallel-sessions.md))

## Resources

- [How Boris Uses Claude Code](https://howborisusesclaudecode.com/)
- [Claude Code Workflows](https://code.claude.com/docs/workflows)
