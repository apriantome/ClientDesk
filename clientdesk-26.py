# === Stage 26: Add weekly summary calculations ===
# Project: ClientDesk
def calculate_weekly_summary(db):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    summary = {
        "week_start": week_start.isoformat(),
        "total_contacts": 0,
        "new_meetings": 0,
        "completed_tasks": 0,
        "pending_tasks": 0,
        "notes_count": 0
    }

    for contact in db["contacts"]:
        summary["total_contacts"] += 1
    
    for meeting in db["meetings"]:
        if week_start <= meeting.get("date", "") < week_end:
            summary["new_meetings"] += 1
            
    for task in db["tasks"]:
        status = task.get("status", "").lower()
        due_date = task.get("due_date", "")
        if status == "completed":
            summary["completed_tasks"] += 1
        elif status == "pending" and (not due_date or week_start <= due_date < week_end):
            summary["pending_tasks"] += 1
            
    for note in db["notes"]:
        if week_start <= note.get("date", "") < week_end:
            summary["notes_count"] += 1

    return summary
