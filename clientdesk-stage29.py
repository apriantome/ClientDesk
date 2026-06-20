# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ClientDesk
from datetime import datetime, timedelta
def get_upcoming_tasks(task_list: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [t for t in task_list if now <= t.get("due_date", now) < cutoff]

def get_upcoming_meetings(meeting_list: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [m for m in meeting_list if now <= m.get("start_time", now) < cutoff]

def get_upcoming_birthdays(contact_list: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [c for c in contact_list if (now <= c.get("birthday", now) < cutoff)]

def get_upcoming_followups(client_history: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [h for h in client_history if now <= h.get("next_contact_date", now) < cutoff]

def format_reminder(item: dict, days_until: int | None = None) -> str:
    due = item.get("due_date") or item.get("start_time") or item.get("birthday") or item.get("next_contact_date")
    if isinstance(due, datetime):
        delta = (due - now).days
        return f"[{delta} days] {item['title']}"
    return str(item)
