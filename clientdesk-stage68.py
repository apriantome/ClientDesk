# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ClientDesk
from datetime import datetime, timedelta
import json
from pathlib import Path

def generate_changelog(log_path: str = "activity.log", output_path: str = "CHANGELOG.md") -> None:
    """Generate a compact changelog from the activity log."""
    entries = []
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) >= 3:
                    date_str, author, msg = parts[:3]
                    entries.append({'date': datetime.strptime(date_str, '%Y-%m-%d'), 'author': author, 'msg': msg})
    except FileNotFoundError:
        return

    if not entries:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Changelog\n")
        return

    entries.sort(key=lambda x: x['date'], reverse=True)
    
    grouped = {}
    for entry in entries:
        key = entry['author']
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(entry)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Changelog\n")
        for author, items in sorted(grouped.items()):
            f.write(f"## {author}\n")
            for item in items[:5]:  # Limit to last 5 entries per author
                date_str = item['date'].strftime('%Y-%m-%d')
                msg = item['msg']
                f.write(f"- **{date_str}**: {msg}\n")

if __name__ == "__main__":
    generate_changelog()
