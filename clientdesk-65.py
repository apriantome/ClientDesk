# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ClientDesk
from typing import Union, Optional
import re
from pathlib import Path


def merge_imports(existing: list[str], new: list[str]) -> tuple[list[str], set[str]]:
    """Merge imports avoiding duplicates and normalizing aliases."""
    normalized = {imp.strip(): imp for imp in existing}
    added_aliases = set()

    def normalize(name: str) -> str:
        match = re.match(r"^(\w+)\s*as\s*(\w+)$", name)
        if match: return f"{match.group(1)} as {match.group(2)}"
        return name.strip()

    for imp in new:
        clean = normalize(imp).strip()
        base, alias = re.split(r"\s+as\s+", clean, maxsplit=1)
        if clean in normalized and (alias is None or normalized[clean].endswith(f" as {alias}")):
            continue
        elif clean.startswith("from"):
            parts = clean.split()
            module = parts[1]
            alias_part = " ".join(parts[2:]) if len(parts) > 2 else ""
            existing_line = normalized.get(module, "")
            if not existing_line or (alias_part and not existing_line.endswith(f" as {alias_part}")):
                normalized[module] = clean
        elif base in normalized and alias is None:
            continue
        else:
            normalized[clean] = clean

    merged = list(normalized.values())
    return sorted(merged), added_aliases
