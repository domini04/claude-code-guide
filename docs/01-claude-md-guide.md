# CLAUDE.md: The Complete Guide

## What is CLAUDE.md?

CLAUDE.md is Claude Code's persistent memory system - a special file automatically loaded into every conversation to provide project-specific context without manual repetition.

Think of it as your project's "constitution" - the primary source of truth for how your repository works.

## The Critical Role

CLAUDE.md solves the repetition problem. Without it, you'd explain:
- "Use bun, not npm" - every session
- "Run tests with `npm test:unit`" - every session
- "Check the API docs before adding endpoints" - every session

With CLAUDE.md, these become permanent context.

## The WHAT, WHY, HOW Framework

Professional CLAUDE.md files follow this three-part structure:

### 1. WHAT - Technology & Structure
Tell Claude about your stack and organization.

```markdown
## Tech Stack
- Frontend: React 18 + TypeScript
- Backend: Node.js + Express
- Database: PostgreSQL with Prisma ORM
- Testing: Jest + React Testing Library

## Project Structure
- `/apps/web` - Main web application
- `/apps/api` - REST API server
- `/packages/ui` - Shared component library
- `/packages/utils` - Shared utilities
```

### 2. WHY - Purpose & Context
Explain what the project does and why components exist.

```markdown
## Purpose
Customer relationship management system for small businesses.
Focus on simplicity and speed over enterprise features.

## Key Components
- `/apps/web/src/features/contacts` - Contact management (core feature)
- `/apps/web/src/features/calendar` - Meeting scheduling (secondary)
- `/packages/ui` - Design system based on Tailwind
```

### 3. HOW - Workflows & Commands
Define how to work on the project.

```markdown
## Commands
- bun run dev: Start development servers (web + API)
- bun run test: Run all tests with coverage
- bun run typecheck: TypeScript validation
- bun run build: Production build

## Workflow
1. IMPORTANT: Run typecheck before committing
2. Write tests for new features
3. Update API docs in `/docs/api` when adding endpoints
```

## Size Guidelines

### Instruction Budget
LLMs can reliably follow ~150-200 instructions. Claude Code's system prompt uses ~50, leaving limited budget for CLAUDE.md.

**Recommended Limits**:
- **Small projects**: 60-100 lines
- **Medium projects**: 100-200 lines
- **Enterprise monorepos**: 200-300 lines (13-25KB)

### Why Size Matters
Claude Code adds a system reminder that context "may or may not be relevant." Non-universal instructions get deprioritized as count increases.

**Keep only universally applicable rules.**

## Progressive Disclosure Pattern

Don't dump everything into CLAUDE.md. Tell Claude where to find detailed information:

```markdown
## Documentation
- IMPORTANT: Read docs/architecture.md before structural changes
- Database schema: See docs/schema.sql and Prisma schema
- API conventions: Check src/api/README.md for patterns
- Component guidelines: See packages/ui/CONTRIBUTING.md

## Code Patterns
- Authentication: Reference src/auth/README.md
- Database queries: Follow patterns in src/db/queries/users.ts
```

This approach:
- Keeps CLAUDE.md concise
- Claude reads details only when needed
- Detailed docs stay up-to-date in their proper locations

## Writing for AI, Not Humans

### Good Examples

**Concise and actionable**:
```markdown
# Commands
- npm run build: Build the project
- npm run test: Run tests with coverage
- npm run dev: Start dev server on port 3000

# Code Style
- Use ES modules (import/export), not CommonJS
- Destructure imports: import { foo } from 'bar'
- Prefer const over let
```

### Bad Examples

**Too verbose**:
```markdown
# Building the Project
When you want to build the project, you should run the build
command. This will compile all TypeScript files and output them
to the dist folder. The build process typically takes 30 seconds...
```

**Non-universal**:
```markdown
# When fixing the login bug
1. Check if the JWT token is expired
2. Verify the refresh token endpoint
3. Update the auth middleware...
```
*(This is task-specific, not universally applicable)*

## What NOT to Include

### ❌ Code Style Guidelines
**Why**: Use linters instead (ESLint, Biome, Prettier)
- LLMs are expensive and slow for style enforcement
- Deterministic tools are faster and more reliable
- Use PostToolUse hooks to auto-format after edits

### ❌ Exhaustive Instructions
**Why**: Instruction overload → Claude ignores everything
- Focus on universal patterns
- Claude learns from existing code
- Don't list every edge case

### ❌ Task-Specific Details
**Why**: Should be temporary context, not permanent
- Bug fixes: Provide context in the conversation
- Feature requests: Describe in the message
- One-time operations: Not in CLAUDE.md

### ❌ Out-of-Date Code Snippets
**Why**: They become stale quickly
- Use `file:line` references instead
- Point to authoritative source code
- Keep single source of truth

## File Location Strategies

### Single Project
```
/project-root/
  CLAUDE.md          ← Check into git (recommended for teams)
  CLAUDE.local.md    ← Add to .gitignore (personal config)
```

### Monorepo (Hierarchical)
```
/monorepo/
  CLAUDE.md                      ← Universal rules for entire repo
  /apps/
    web/CLAUDE.md                ← Web app specific rules
    api/CLAUDE.md                ← API specific rules
  /packages/
    ui/CLAUDE.md                 ← UI library specific rules
```

Claude reads all applicable files in the hierarchy.

### Global Configuration
```
~/.claude/CLAUDE.md              ← Applies to all projects
```

Use for universal personal preferences (editor choice, style preferences).

## Professional Examples

### Boris Cherny's Team (Anthropic)
**Size**: 13KB (could grow to 25KB)
**Rule**: Only document tools/APIs used by 30%+ of engineers
**Updates**: Multiple times weekly
**Philosophy**: "When Claude makes mistakes, add to CLAUDE.md"

### Enterprise Pattern
```markdown
# Monorepo Structure
- apps/web - Customer-facing web app (Next.js)
- apps/admin - Internal admin dashboard (Next.js)
- apps/api - GraphQL API (Node.js)
- packages/* - Shared libraries

# Important Rules
- IMPORTANT: Never commit secrets to git
- IMPORTANT: Run `pnpm typecheck` before pushing
- IMPORTANT: Update CHANGELOG.md for user-facing changes

# Common Commands
- pnpm install: Install dependencies
- pnpm dev: Start all apps in dev mode
- pnpm test: Run all tests
- pnpm build: Build all packages and apps

# Architecture Decisions
- State management: Zustand (not Redux)
- Styling: Tailwind (no CSS-in-JS)
- Date handling: date-fns (not moment)
- Forms: React Hook Form + Zod validation

# Documentation
- Architecture overview: docs/architecture.md
- Database schema: docs/database.md
- API documentation: apps/api/docs/graphql.md
```

### Solo Developer Pattern
```markdown
# Personal Project

## Stack
- SvelteKit + TypeScript
- SQLite with Drizzle ORM
- Tailwind CSS

## Commands
- npm run dev: Dev server on localhost:5173
- npm run test: Vitest unit tests
- npm run check: Type checking + linting

## Patterns
- Server code in src/routes/+page.server.ts
- Components in src/lib/components/
- Utilities in src/lib/utils/

## Verification
- IMPORTANT: Run `npm run check` after changes
- Test in browser at localhost:5173
```

## The `#` Key Technique

During a coding session, press `#` to have Claude suggest additions to CLAUDE.md based on current context.

**Example workflow**:
1. Working on authentication feature
2. Claude learns your JWT preferences
3. Press `#`
4. Claude suggests: "Add 'Use JWT with 7-day expiry' to CLAUDE.md"
5. Review and accept

## Update Workflow

### When to Update

**Update immediately when**:
1. Claude makes the same mistake twice
2. You explain the same context repeatedly
3. New team member needs onboarding info
4. Architecture or conventions change
5. New tools or workflows adopted

### Team Update Pattern (Boris's Approach)

```markdown
# During Code Review
1. Reviewer notices pattern issue
2. Tags @.claude in PR comment
3. GitHub Action updates CLAUDE.md
4. Team benefits from learning
5. Pattern becomes permanent
```

Set up with `.github/workflows/claude-md-update.yml`

### Solo Update Pattern

```markdown
# After Completing Work
1. Reflect: "What did I explain to Claude today?"
2. Open CLAUDE.md
3. Add universal patterns
4. Remove outdated info
5. Commit with message: "docs: update CLAUDE.md with [pattern]"
```

## Verification Integration

The most important addition: Tell Claude how to verify its work.

```markdown
# Verification (IMPORTANT)
- After code changes: Run `npm run typecheck`
- After UI changes: Test in browser at http://localhost:3000
- After API changes: Run `npm run test:api`
- Before committing: Run `npm run lint`
- Check console for errors in dev mode

## Verification Standards
- All tests must pass
- No TypeScript errors
- No console errors in browser
- Responsive design works on mobile (use DevTools)
```

This creates the feedback loop that 2-3x quality.

## Common Mistakes

### 1. Information Overload
**Symptom**: CLAUDE.md is 500+ lines
**Fix**: Extract details to separate docs, keep universal rules only

### 2. Never Updating
**Symptom**: Created once, never touched again
**Fix**: Treat as living document, update weekly

### 3. Duplicating Linters
**Symptom**: "Always use semicolons" in CLAUDE.md
**Fix**: Configure ESLint, add PostToolUse hook to auto-format

### 4. Task-Specific Instructions
**Symptom**: "For the login bug, check JWT expiry"
**Fix**: Provide in conversation, not CLAUDE.md

### 5. No Verification Steps
**Symptom**: Missing the quality multiplier
**Fix**: Add verification section first

## Quick Start Template

```markdown
# [Project Name]

## Purpose
[One sentence describing what this project does]

## Tech Stack
- [List key technologies]

## Project Structure
- [Key directories and their purposes]

## Commands
- [command]: [What it does]

## Workflow
1. IMPORTANT: [Critical steps]
2. [Standard process]

## Verification
- After changes: [How to verify]
- Before commit: [What to check]

## Documentation
- [Topic]: See [file path]
```

## Advanced: Prompt Engineering

Use emphasis for critical rules:

```markdown
# CRITICAL RULES
- NEVER commit .env files
- ALWAYS run tests before pushing
- MUST update API docs when adding endpoints

# Important Guidelines
- Prefer functional components over class components
- Use TypeScript strict mode
```

Keywords like "IMPORTANT", "NEVER", "ALWAYS", "MUST", "CRITICAL" improve adherence.

## Refinement Process

Treat CLAUDE.md like a prompt:

1. **Observe**: How does Claude behave?
2. **Adjust**: Add/remove/reword instructions
3. **Test**: Does behavior improve?
4. **Iterate**: Refine over time

Optional: Run through Anthropic's prompt improver tool periodically.

## Next Steps

1. **Create**: Start with the Quick Start Template
2. **Use**: Run Claude Code sessions and observe
3. **Refine**: Update when Claude misunderstands
4. **Verify**: Add verification steps (see [06-verification-quality.md](06-verification-quality.md))
5. **Automate**: Pair with hooks (see [04-hooks-automation.md](04-hooks-automation.md))

## Resources

- [Writing a good CLAUDE.md - HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Using CLAUDE.MD files - Claude Blog](https://claude.com/blog/using-claude-md-files)
- [Best Practices - Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
