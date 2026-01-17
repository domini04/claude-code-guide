---
description: "Debug workflow for errors"
---

Debug the specified error or issue systematically.

## Debug Process

1. **Understand the Error**
   - Parse the stack trace or error message
   - Identify the failing file and line number
   - Understand what operation failed

2. **Reproduce**
   - Identify minimal reproduction steps
   - Run the failing test or command

3. **Root Cause Analysis**
   - Trace the code path that led to the error
   - Check for:
     - Missing null checks
     - Type mismatches
     - Incorrect assumptions
     - Race conditions
     - Missing dependencies

4. **Implement Fix**
   - Make the minimal change needed
   - Avoid introducing new issues

5. **Verify**
   - Run the failing test again
   - Run related tests
   - Ensure no regressions

## Output

- Root cause explanation
- Fix applied with `file:line` reference
- Verification results

$ARGUMENTS
