# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ClientDesk
SETTINGS_FILE = "settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "theme": "light",
            "default_timezone": "UTC",
            "notification_sound": True,
            "max_history_days": 365
        }

def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2)

def update_setting(key, value):
    settings = load_settings()
    if key in settings:
        settings[key] = value
        save_settings(settings)
        return True
    else:
        print(f"Error: Setting '{key}' does not exist.")
        return False

def get_setting(key, default=None):
    settings = load_settings()
    return settings.get(key, default)
