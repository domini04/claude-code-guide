---
description: "Run full verification suite"
---

Execute the complete verification checklist. Stop on first failure.

## Steps

1. **Lint Check**
   ```bash
   ruff check src/
   ```
   Report: PASS or list errors with `file:line`

2. **Format Check**
   ```bash
   ruff format --check src/
   ```
   Report: PASS or list files needing formatting

3. **Type Check**
   ```bash
   mypy src/ --ignore-missing-imports
   ```
   Report: PASS or list type errors

4. **Test Suite**
   ```bash
   pytest --cov=src --cov-fail-under=70
   ```
   Report: PASS with coverage % or list failures

## Summary

At the end, provide:
- Overall: PASS/FAIL
- Any issues found with `file:line` references
- Suggested next steps if failed
