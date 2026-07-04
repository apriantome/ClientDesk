# === Stage 67: Add a function that returns key project metrics ===
# Project: ClientDesk
def get_project_metrics(db):
    """Calculate and return key project metrics from the database."""
    total_contacts = sum(1 for _ in db.query("SELECT 1 FROM contacts"))
    active_clients = sum(1 for c in db.query("SELECT * FROM clients WHERE status='active'") if c)
    pending_tasks = sum(1 for t in db.query("SELECT * FROM tasks WHERE status='pending'") if t)
    completed_meetings = sum(1 for m in db.query("SELECT * FROM meetings WHERE status='completed'") if m)
    total_revenue = sum(c.get('revenue', 0) or 0 for c in db.query("SELECT * FROM clients"))
    avg_response_time = None
    responses = db.query("SELECT response_time FROM interactions WHERE type='email'")
    if responses:
        avg_response_time = sum(r.response_time for r in responses) / len(responses)
    return {
        "total_contacts": total_contacts,
        "active_clients": active_clients,
        "pending_tasks": pending_tasks,
        "completed_meetings": completed_meetings,
        "total_revenue": total_revenue,
        "avg_response_time_sec": round(avg_response_time, 2) if avg_response_time else None
    }
