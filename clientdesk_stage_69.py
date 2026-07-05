# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ClientDesk
import json, os, sys
from pathlib import Path

def reset_demo_data():
    script_dir = Path(__file__).parent.resolve()
    db_file = script_dir / "clients.json"
    if not db_file.exists():
        print("Error: clients.json not found.")
        return 1
    
    demo_clients = [
        {"id": 1, "name": "Иван Иванов", "phone": "+79001234567", "status": "active"},
        {"id": 2, "name": "Мария Петрова", "phone": "+79007654321", "status": "lead"},
        {"id": 3, "name": "ООО Вектор", "phone": "+79001112233", "status": "client"}
    ]

    try:
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(demo_clients, f, ensure_ascii=False, indent=4)
        print(f"Demo data reset successfully to {db_file}")
        return 0
    except Exception as e:
        print(f"Error resetting demo data: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(reset_demo_data())
