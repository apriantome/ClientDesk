# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ClientDesk
import json
from datetime import datetime, timedelta
from typing import Optional

class ClientDesk:
    def __init__(self):
        self.contacts = {}
        self.meetings = []
        self.tasks = []
        self.history = []

    def add_contact(self, name: str, phone: str, email: str = ""):
        self.contacts[name] = {"phone": phone, "email": email}

    def schedule_meeting(self, client_name: str, date: datetime, topic: str):
        self.meetings.append({
            "client": client_name,
            "date": date.isoformat(),
            "topic": topic
        })

    def add_task(self, description: str, deadline: datetime, priority: int = 1):
        self.tasks.append({
            "description": description,
            "deadline": deadline.isoformat(),
            "priority": priority
        })

    def log_event(self, event_type: str, details: dict):
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "details": details
        })

    def get_overview(self) -> dict:
        return {
            "contacts_count": len(self.contacts),
            "meetings_count": len(self.meetings),
            "tasks_count": len(self.tasks),
            "history_count": len(self.history)
        }

# Demo dataset initialization
desk = ClientDesk()
desk.add_contact("Ivanov", "+79001234567", "ivan@example.com")
desk.add_contact("Petrov", "+79007654321")
desk.schedule_meeting("Ivanov", datetime.now() + timedelta(days=1), "Contract review")
desk.add_task("Send invoice #1024", datetime.now() + timedelta(hours=2), priority=2)
desk.log_event("system_start", {"version": "1.0"})
