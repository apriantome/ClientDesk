# === Stage 42: Add CSV export without external dependencies ===
# Project: ClientDesk
def export_to_csv(data, filename="clients.csv"):
    import csv
    if not data: return False
    headers = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return True
