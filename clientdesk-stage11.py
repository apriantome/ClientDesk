# === Stage 11: Add JSON export for the current application state ===
# Project: ClientDesk
import json, os
from pathlib import Path

def export_state(db_path: str) -> None:
    """Export current application state to a JSON file."""
    if not os.path.exists(db_path):
        return
    
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    output_dir = Path(__file__).parent / "exports"
    output_dir.mkdir(exist_ok=True)
    
    filename = output_dir / f"state_{int(time.time())}.json"
    with open(filename, 'w', encoding='utf-8') as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
