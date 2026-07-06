# === Stage 72: Add Markdown report export ===
# Project: ClientDesk
def export_markdown_report(self, filename=None):
    if filename is None:
        filename = f"report_{datetime.now():%Y%m%d}.md"
    lines = []
    lines.append(f"# ClientDesk Report — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    for name, section in self._sections.items():
        if isinstance(section, list):
            lines.append(f"\n## {name}")
            for item in section:
                lines.append(f"- {item}\n")
        else:
            lines.append(f"\n## {name}: {section}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
