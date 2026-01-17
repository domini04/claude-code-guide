---
description: "Code review workflow"
---

Perform a comprehensive code review of the current changes or specified files.

## Review Process

1. **Identify Changes**
   - Run `git diff` to see uncommitted changes
   - If no changes, review files specified in arguments

2. **Security Review**
   - SQL injection vulnerabilities
   - Input validation gaps
   - Sensitive data exposure
   - Authentication/authorization issues

3. **Code Quality Review**
   - Error handling completeness
   - Code duplication
   - Function complexity
   - Naming conventions

4. **Test Coverage**
   - Are new features tested?
   - Are edge cases covered?
   - Integration test needs?

## Output Format

Provide structured feedback:

### Critical (Must Fix)
- `file:line` - Issue description

### Warnings (Should Fix)
- `file:line` - Issue description

### Suggestions (Consider)
- `file:line` - Improvement idea

$ARGUMENTS
