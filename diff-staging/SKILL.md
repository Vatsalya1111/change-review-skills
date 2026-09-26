---
name: diff-staging
description: Apply proposed Python code changes only inside the sandbox and return the resulting Git diff and changed-file metadata.
---

# Diff Staging Skill

## Goal

Create and inspect the proposed code change safely inside the sandbox without changing the real working tree or GitHub repository.

## Procedure

1. Work only inside the sandbox copy of the repository.
2. Record the baseline commit or baseline Git state.
3. Apply the proposed modification in the sandbox.
4. Run `git status --short`.
5. Run `git diff --no-ext-diff`.
6. Identify changed files.
7. Record additions and deletions.
8. Return the patch and metadata as structured JSON.

## Output format

Return:

{
  "base_commit": "",
  "changed_files": [
    {
      "path": "discount.py",
      "insertions": 1,
      "deletions": 1
    }
  ],
  "insertions": 1,
  "deletions": 1,
  "patch": ""
}

## Rules

- Never modify the original GitHub repository before approval.
- Never modify the user's real working tree.
- Perform all proposed edits in the sandbox.
- Return the actual `git diff`.
- Do not invent changed lines or files.
