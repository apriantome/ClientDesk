# === Stage 14: Add file load support with fallback demo data ===
# Project: ClientDesk
import json, os

def load_data(path='data.json'):
    try:
        with open(path) as f: return json.load(f)
    except FileNotFoundError:
        demo = {
            "contacts": [{"id": 1, "name": "Иван Иванов", "phone": "+79001234567"}],
            "meetings": [],
            "tasks": []
        }
        os.makedirs(os.path.dirname(path), exist_ok=True) if path != 'data.json' else None
        with open(path, 'w') as f: json.dump(demo, f)
        return demo
