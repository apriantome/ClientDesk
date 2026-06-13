# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ClientDesk
import json, os

def load_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        error_msg = str(e).split("'")[1].replace("'", "") if "'" in str(e) else str(e)
        print(f"[ERROR] Malformed JSON at {path}: {error_msg[:50]}...")
        return {}

def save_json_safe(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save {path}: {e}")
        return False

def merge_json_files(base_path, update_path):
    base = load_json_safe(base_path)
    updates = load_json_safe(update_path)
    if not updates:
        return base
    
    for key in updates:
        if key not in base:
            base[key] = {}
        # Simple merge strategy: overwrite or extend lists
        val_base = base[key]
        val_upd = updates[key]
        
        if isinstance(val_base, dict) and isinstance(val_upd, dict):
            for k_v, v_v in val_upd.items():
                base[key][k_v] = v_v
        elif isinstance(val_base, list) and isinstance(val_upd, list):
            # Append unique items to avoid duplicates
            existing_ids = {item.get('id') or item.get('_id') for item in val_base if isinstance(item, dict)}
            for item in val_upd:
                uid = item.get('id') or item.get('_id')
                if uid not in existing_ids:
                    base[key].append(item)
        else:
            # Direct overwrite for non-list/non-dict values
            base[key] = val_upd
    
    return base
