# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ClientDesk
def snapshot_diff(before: dict, after: dict) -> dict:
    """Compare two snapshots and return a structured diff of changed fields."""
    all_keys = set(before.keys()) | set(after.keys())
    changes = {}
    for key in sorted(all_keys):
        old_val = before.get(key)
        new_val = after.get(key)
        if old_val == new_val:
            continue
        if isinstance(old_val, dict) and isinstance(new_val, dict):
            changes[key] = snapshot_diff(old_val, new_val)
        else:
            changes[key] = {"before": old_val, "after": new_val}
    return changes


def print_snapshot_report(before_state: dict, after_state: dict) -> str:
    """Generate a human-readable report of state transitions."""
    diff = snapshot_diff(before_state, after_state)
    lines = ["=== Snapshot Comparison ===", f"Total changed fields: {len(diff)}"]
    for field, change in sorted(diff.items()):
        if isinstance(change, dict):
            lines.append(f"\n{field}:")
            if "before" in change and "after" in change:
                lines.append(f"  Before: {change['before']}")
                lines.append(f"  After:  {change['after']}")
        else:
            lines.append(f"  {field}: {change}")
    return "\n".join(lines)
