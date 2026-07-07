# === Stage 73: Add a lightweight HTML report export ===
# Project: ClientDesk
import json, datetime, pathlib

def export_report(db_path: str = "data/clientdesk.db", out_dir: str = "reports") -> str:
    """Export a lightweight HTML report from the ClientDesk SQLite database."""
    db_path = pathlib.Path(db_path)
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()

    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]

    rows_html = ""
    for table_name in sorted(tables):
        cur.execute(f"SELECT * FROM [{table_name}] LIMIT 50")
        cols = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        if not data:
            continue
        header = "<tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>"
        body = ""
        for row in data:
            cells = "".join("<td>" + str(row[c]) + "</td>" for c in cols)
            body += "<tr>" + cells + "</tr>"
        rows_html += f"<h2>{table_name}</h2><table border='1'><thead><tr>{header}</tr></thead><tbody>{body}</tbody></table>\n"

    html = (f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>ClientDesk Report</title></head>
<body style="font-family: sans-serif; max-width: 900px; margin: auto;">
<h1>ClientDesk Report — {today}</h1>
<p>Total contacts: <strong>{cur.execute("SELECT COUNT(*) FROM contacts").fetchone()[0]}</strong></p>
{rows_html}
</body></html>""")

    out_path = out_dir / f"report_{today}.html"
    out_path.write_text(html)
    conn.close()
    return str(out_path.resolve())
