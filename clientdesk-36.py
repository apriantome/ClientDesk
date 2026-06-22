# === Stage 36: Add templates for quickly creating common records ===
# Project: ClientDesk
from datetime import date, timedelta
def create_contact(name: str, phone: str) -> dict: return {"id": len(contacts)+1, "name": name, "phone": phone}
def create_meeting(client_id: int, topic: str, scheduled_at: date = None) -> dict: 
    if not scheduled_at: scheduled_at = date.today() + timedelta(days=7)
    return {"id": len(meetings)+1, "client_id": client_id, "topic": topic, "scheduled_at": scheduled_at}
def create_task(description: str, due_date: date = None, priority: int = 3) -> dict: 
    if not due_date: due_date = date.today() + timedelta(days=2)
    return {"id": len(tasks)+1, "description": description, "due_date": due_date, "priority": priority}
def create_note(client_id: int, content: str, created_at: date = None) -> dict: 
    if not created_at: created_at = date.today()
    return {"id": len(history)+1, "client_id": client_id, "content": content, "created_at": created_at}
