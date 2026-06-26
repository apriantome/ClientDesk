# === Stage 45: Add restore from backup with validation ===
# Project: ClientDesk
import json, os, shutil
from datetime import datetime

BACKUP_FILE = "backup.json"
DATA_DIR = "data"

def restore_backup(backup_path: str) -> bool:
    if not os.path.exists(backup_path):
        print(f"[WARN] Backup file '{backup_path}' not found.")
        return False
    
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        required_keys = {"contacts", "meetings", "tasks"}
        if not required_keys.issubset(data.keys()):
            print("[ERROR] Backup missing required keys.")
            return False
        
        backup_time = datetime.fromisoformat(data.get("timestamp", ""))
        current_data_path = os.path.join(DATA_DIR, "db.json")
        
        if os.path.exists(current_data_path):
            with open(current_data_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
            
            # Validate backup is newer or same size to prevent accidental overwrites of larger DBs
            if len(json.dumps(data)) < len(json.dumps(existing_data)):
                print("[WARN] Backup appears smaller than current data. Skipping restore.")
                return False
        
        shutil.copy(backup_path, current_data_path)
        print(f"[OK] Restored from '{backup_path}' at {datetime.now().isoformat()}")
        return True

    except json.JSONDecodeError:
        print("[ERROR] Backup file is corrupted or invalid JSON.")
        return False
    except Exception as e:
        print(f"[ERROR] Restore failed: {e}")
        return False
