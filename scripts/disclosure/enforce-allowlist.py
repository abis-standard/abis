#!/usr/bin/env python3
"""M229D-001 — Public allowlist enforcement. Generic errors only."""
from __future__ import annotations

import fnmatch
import sys
from pathlib import Path


def load_allowed_paths(allowlist_path: Path) -> list[str]:
    allowed: list[str] = []
    in_allowed = False
    for line in allowlist_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("allowed_paths:"):
            in_allowed = True
            continue
        if in_allowed:
            if stripped.startswith("- "):
                allowed.append(stripped[2:].strip())
            elif stripped and not stripped.startswith("#") and ":" in stripped:
                break
    return allowed


def is_allowed(rel: str, patterns: list[str]) -> bool:
    rel = rel.replace("\\", "/")
    for pattern in patterns:
        pattern = pattern.replace("\\", "/")
        if fnmatch.fnmatch(rel, pattern):
            return True
        # Directory glob support
        if pattern.endswith("/**"):
            prefix = pattern[:-3]
            if rel == prefix or rel.startswith(prefix + "/"):
                return True
    return False


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    allowlist = repo_root / "public-allowlist.yml"
    if not allowlist.exists():
        print("M229D-001 REVIEW_REQUIRED: allowlist unavailable", file=sys.stderr)
        return 3

    patterns = load_allowed_paths(allowlist)
    if not patterns:
        print("M229D-001 REVIEW_REQUIRED: allowlist empty", file=sys.stderr)
        return 3

    unknown: list[str] = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root).as_posix()
        if rel.startswith(".git/"):
            continue
        if not is_allowed(rel, patterns):
            unknown.append(rel)

    if unknown:
        print("M229D-001 BLOCK: Disclosure policy violation detected.", file=sys.stderr)
        print(f"Unexpected file count: {len(unknown)}", file=sys.stderr)
        return 1

    print("M229D-001 PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
