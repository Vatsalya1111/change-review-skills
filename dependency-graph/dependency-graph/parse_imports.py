from pathlib import Path
import ast
import json
import sys


def module_name_from_path(root: Path, path: Path) -> str:
    relative = path.relative_to(root).with_suffix("")
    parts = list(relative.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]

    return ".".join(parts)


def collect_python_files(root: Path):
    result = []

    for path in root.rglob("*.py"):
        if ".git" in path.parts:
            continue

        result.append(path)

    return sorted(result)


def extract_import_names(path: Path):
    try:
        tree = ast.parse(
            path.read_text(encoding="utf-8")
        )
    except (SyntaxError, UnicodeDecodeError):
        return []

    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            imports.extend(
                alias.name
                for alias in node.names
            )

        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                imports.append(node.module)

    return imports


def main():

    root = Path(
        sys.argv[1] if len(sys.argv) > 1 else "."
    ).resolve()

    files = collect_python_files(root)

    module_to_path = {
        module_name_from_path(root, path): path
        for path in files
    }

    nodes = []
    edges = []

    for path in files:

        relative = path.relative_to(root).as_posix()

        nodes.append({
            "file": relative
        })

        for imported in extract_import_names(path):

            target_path = module_to_path.get(imported)

            if target_path is None:

                first = imported.split(".")[0]

                target_path = module_to_path.get(first)

            if target_path is not None and target_path != path:

                target_relative = (
                    target_path
                    .relative_to(root)
                    .as_posix()
                )

                edges.append({
                    "from": relative,
                    "to": target_relative,
                    "relationship": "imports"
                })

    print(
        json.dumps(
            {
                "nodes": nodes,
                "edges": edges
            },
            indent=2
        )
    )


if __name__ == "__main__":
    main()
