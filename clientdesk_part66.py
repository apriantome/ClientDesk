# === Stage 66: Add export of a short status dashboard ===
# Project: ClientDesk
def export_dashboard():
    from datetime import datetime, timedelta
    today = datetime.now().date()
    yesterday = (today - timedelta(days=1)).isoformat()
    week_ago = (today - timedelta(weeks=1)).isoformat()
    
    contacts_count = len(db.get('contacts', []))
    meetings_today = sum(1 for m in db.get('meetings', []) if datetime.fromisoformat(m['date']).date() == today)
    tasks_overdue = sum(1 for t in db.get('tasks', []) if t['status'] != 'done' and t['deadline'] <= yesterday)
    
    history_entries = len(db.get('history', []))
    
    print(f"=== ClientDesk Status ({today.isoformat()}) ===")
    print(f"Contacts: {contacts_count}")
    print(f"Meetings Today: {meetings_today}")
    print(f"Overdue Tasks: {tasks_overdue}")
    print(f"History Entries: {history_entries}")
