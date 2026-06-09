# === Stage 4: Implement create operations for the primary records ===
# Project: ClientDesk
from datetime import datetime, timedelta
import uuid

def create_contact(name: str, phone: str, email: str = "") -> dict:
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "phone": phone,
        "email": email,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

def create_meeting(contact_id: str, title: str, start_time: datetime, end_time: datetime) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "contact_id": contact_id,
        "title": title,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "status": "scheduled",
        "created_at": datetime.now().isoformat()
    }

def create_task(contact_id: str, description: str, due_date: datetime) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "contact_id": contact_id,
        "description": description,
        "due_date": due_date.isoformat(),
        "status": "pending",
        "priority": "medium",
        "created_at": datetime.now().isoformat()
    }

def create_note(contact_id: str, content: str) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "contact_id": contact_id,
        "content": content,
        "created_at": datetime.now().isoformat()
    }
