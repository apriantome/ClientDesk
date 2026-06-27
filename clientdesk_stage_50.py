# === Stage 50: Add unit tests for import and export behavior ===
# Project: ClientDesk
import json, os, tempfile
from pathlib import Path
from typing import List, Dict, Any

def test_import_export():
    temp_dir = tempfile.mkdtemp()
    db_path = Path(temp_dir) / "clients.json"
    
    # Setup initial data
    initial_data = {
        "contacts": [{"id": 1, "name": "Alice", "email": "alice@test.com"}],
        "meetings": [],
        "tasks": []
    }
    with open(db_path, "w") as f:
        json.dump(initial_data, f)

    # Test import from file
    imported = ClientDesk.import_db(str(db_path))
    assert len(imported["contacts"]) == 1
    assert imported["contacts"][0]["name"] == "Alice"

    # Test export to new file
    exported_path = Path(temp_dir) / "export.json"
    ClientDesk.export_db(exported_path, initial_data)
    
    with open(exported_path, "r") as f:
        exported_content = json.load(f)
    
    assert len(exported_content["contacts"]) == 1
    assert exported_content["contacts"][0]["name"] == "Alice"

    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)
