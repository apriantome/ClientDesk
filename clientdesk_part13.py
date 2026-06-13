# === Stage 13: Add file save support using a configurable path ===
# Project: ClientDesk
import os, json, sys
from pathlib import Path

def get_config_path():
    base = Path.home() / ".clientdesk"
    if not base.exists():
        base.mkdir(parents=True)
    return str(base / "config.json")

def save_state(data):
    path = get_config_path()
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved to {path}")
    except Exception as e:
        sys.stderr.write(f"Save error: {e}\n")

def load_state():
    path = get_config_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}
