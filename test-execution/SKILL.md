---
name: test-execution
description: Run the existing Python test suite inside the sandbox and return structured per-test results.
---

# Test Execution Skill

## Goal

Run the repository's existing tests against the proposed change inside the sandbox and return machine-readable results.

## Procedure

1. Work only inside the sandbox.
2. Inspect the repository for its existing test setup.
3. Prefer `pytest` when it is available.
4. Run the existing test suite against the staged change.
5. Capture the actual test output.
6. Record passed, failed, and skipped tests.
7. Associate a failure with relevant files when this can be established from the traceback.
8. Return structured JSON.

## Output format

Return:

{
  "status": "passed|failed|error",
  "passed": 0,
  "failed": 0,
  "skipped": 0,
  "tests": [
    {
      "name": "tests/test_example.py::test_example",
      "status": "passed|failed|skipped",
      "files": [],
      "error": null
    }
  ]
}

## Rules

- Report actual test results. Never invent results.
- Do not change tests merely to make the suite pass.
- Do not modify the original GitHub repository.
- Do not hide failures.
- Keep the demo scope to the repository's existing Python test suite.
