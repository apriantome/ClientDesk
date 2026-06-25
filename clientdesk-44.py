# === Stage 44: Add backup creation for the data file ===
# Project: ClientDesk
import os, json, datetime

def backup_data(file_path):
    if not os.path.exists(file_path): return False
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(file_path)}.{timestamp}.bak"
    try:
        with open(file_path, "r", encoding="utf-8") as src, \
             open(backup_name, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        print(f"[Backup] Created {backup_name}")
        return True
    except Exception as e:
        print(f"[Error] Backup failed: {e}")
        return False
