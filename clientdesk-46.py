# === Stage 46: Add a schema version field and migration helper ===
# Project: ClientDesk
from pathlib import Path
import json, uuid
VERSION = "1.1"
MIGRATIONS = {
    1: lambda db: (db.setdefault("schema_version", VERSION), None)
}
def migrate(db_path):
    path = Path(db_path)
    if not path.exists(): return
    data = json.loads(path.read_text())
    current = data.get("schema_version", "0")
    for ver, func in sorted(MIGRATIONS.items()):
        if int(ver) > int(current):
            db["schema_version"] = str(ver)
            func(data)
            path.write_text(json.dumps(data, indent=2))
