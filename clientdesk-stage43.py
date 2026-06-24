# === Stage 43: Add CSV import for the primary record type ===
# Project: ClientDesk
import csv, io

def import_contacts(csv_text: str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(csv_text))
    return [
        {
            "id": f"imp_{i}",
            **{k.strip(): v for k, v in row.items() if k and v}
        }
        for i, row in enumerate(reader)
    ]

def import_meetings(csv_text: str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(csv_text))
    return [
        {
            "id": f"imp_{i}",
            **{k.strip(): v for k, v in row.items() if k and v}
        }
        for i, row in enumerate(reader)
    ]

def import_tasks(csv_text: str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(csv_text))
    return [
        {
            "id": f"imp_{i}",
            **{k.strip(): v for k, v in row.items() if k and v}
        }
        for i, row in enumerate(reader)
    ]
