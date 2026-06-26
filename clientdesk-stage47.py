# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ClientDesk
import random
from datetime import timedelta, date
from typing import List, Dict

def run_demo_scenario(db: Dict) -> None:
    """Executes a full workflow demo: create client, schedule meeting, assign task, log history."""
    # 1. Create new contact
    db["contacts"][f"demo_{random.randint(1000,9999)}"] = {
        "name": f"Demo Client {random.randint(1,50)}",
        "email": f"demo{random.randint(1,50)}@example.com",
        "phone": "+7 (999) 000-0000"
    }

    # 2. Schedule a meeting for next week
    tomorrow = date.today() + timedelta(days=random.randint(3,7))
    db["meetings"][f"{tomorrow.isoformat()}_{random.randint(1,5)}"] = {
        "client_id": list(db["contacts"].keys())[-1],
        "date": str(tomorrow),
        "time": f"{random.choice(['09:00', '14:30'])}",
        "topic": "Initial consultation",
        "status": "scheduled"
    }

    # 3. Create a follow-up task
    db["tasks"][f"task_{len(db['tasks'])+1}"] = {
        "client_id": list(db["contacts"].keys())[-1],
        "description": "Prepare proposal for meeting",
        "due_date": str(tomorrow),
        "status": "pending"
    }

    # 4. Log history entry
    db["history"][f"{tomorrow.isoformat()}_{random.randint(1,5)}"] = {
        "client_id": list(db["contacts"].keys())[-1],
        "action": "meeting_scheduled",
        "details": f"Meeting created for {db['meetings'][list(db['meetings'].keys())[-1]]['topic']}"
    }

    print("Demo scenario completed successfully.")
