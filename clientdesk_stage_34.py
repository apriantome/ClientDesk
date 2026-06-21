# === Stage 34: Add support for multiple local user profiles ===
# Project: ClientDesk
import json, os
from pathlib import Path
PROFILE_DIR = Path(__file__).parent / ".profiles"
def load_profiles(): return {p.stem: p for p in PROFILE_DIR.glob("*.json")} if PROFILE_DIR.exists() else {}
def save_profile(name, data): (PROFILE_DIR / f"{name}.json").write_text(json.dumps(data, indent=2))
def get_current_user(): return os.environ.get("CLIENTDESK_USER") or "default"
def switch_user(user: str):
    if not load_profiles().get(user): raise ValueError(f"No profile for '{user}' found.")
    save_profile(user, {"settings": {}, "contacts": [], "meetings": [], "tasks": []})
    os.environ["CLIENTDESK_USER"] = user
