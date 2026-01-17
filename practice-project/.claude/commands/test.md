---
description: "Run pytest with coverage"
---

Run the test suite with coverage reporting:

1. Execute: `pytest --cov=src --cov-report=term-missing -v`
2. If tests fail:
   - Report each failure with `file:line` reference
   - Show the assertion error message
   - Suggest a fix for each failure
3. If tests pass:
   - Report coverage percentage
   - Identify files with low coverage (<80%)

$ARGUMENTS
