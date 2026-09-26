---
name: dependency-graph
description: Analyze Python file dependencies and produce a structured one-level dependency graph for changed files.
---

# Dependency Graph Skill

Work only inside the sandbox repository.

## Goal

Determine which Python files directly depend on the files changed by a proposed code modification.

## Procedure

1. Identify the file or files changed by the proposed modification.
2. Run the bundled `parse_imports.py` script from this skill.
3. Inspect the local Python import relationships.
4. Identify direct dependents of the changed files.
5. Identify one-level indirect dependents when they are visible from the dependency graph.
6. Return structured JSON only for the analysis result.

## Output format

Return:

{
  "changed_files": [
    {
      "file": "discount.py",
      "status": "changed",
      "reason": "Directly modified"
    }
  ],
  "affected_files": [
    {
      "file": "cart.py",
      "status": "affected",
      "reason": "Depends on discount.py"
    }
  ],
  "nodes": [
    {
      "file": "discount.py",
      "status": "changed",
      "reason": "Directly modified"
    },
    {
      "file": "cart.py",
      "status": "affected",
      "reason": "Direct dependency"
    }
  ],
  "edges": [
    {
      "from": "discount.py",
      "to": "cart.py",
      "relationship": "imported_by"
    }
  ]
}

## Rules

- Work only inside the sandbox.
- Do not modify the original GitHub repository.
- Do not invent dependencies.
- Prefer evidence from actual source imports.
- Keep the demo scope to Python and one dependency level.
