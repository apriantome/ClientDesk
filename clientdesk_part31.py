# === Stage 31: Add compact table rendering for long lists ===
# Project: ClientDesk
def render_compact_table(items, columns):
    if not items: return "No data"
    widths = [max(len(str(item.get(col))) for item in items) + 2 for col in columns]
    header = " | ".join(f"{col:<{widths[i]}}" for i, col in enumerate(columns))
    separator = "-+-".join("-" * w for w in widths)
    lines = [header, separator]
    for item in items:
        row = "".join(str(item.get(col, "")) + " " * (widths[i] - len(str(item.get(col, "")))) 
                      for i, col in enumerate(columns))
        lines.append(row.strip())
    return "\n".join(lines)
