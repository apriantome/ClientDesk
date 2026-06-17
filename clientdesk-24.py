# === Stage 24: Add grouped summaries by category or status ===
# Project: ClientDesk
def generate_grouped_summary(records, group_by='status'):
    groups = {}
    for r in records:
        key = r.get(group_by)
        if key is None: continue
        if key not in groups: groups[key] = []
        groups[key].append(r)
    
    summary_lines = ["# Grouped Summary"]
    for status, items in sorted(groups.items()):
        count = len(items)
        latest_date = max(i.get('date') or '' for i in items if isinstance(i.get('date'), str))
        summary_lines.append(f"\n## {status} ({count})")
        for item in items:
            name = item.get('name', 'Unknown')
            notes = item.get('notes', '')[:50] + ('...' if len(item.get('notes','')) > 50 else '')
            summary_lines.append(f"- **{name}**: {latest_date} — {notes}")
    return "\n".join(summary_lines)
