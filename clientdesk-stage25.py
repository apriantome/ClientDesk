# === Stage 25: Add daily summary calculations ===
# Project: ClientDesk
def calculate_daily_summary(data):
    today = datetime.date.today()
    summary = {"contacts": 0, "meetings": 0, "tasks_completed": 0, "revenue_potential": 0}
    for record in data:
        if isinstance(record, dict) and "date" in record:
            rec_date = datetime.datetime.strptime(record["date"], "%Y-%m-%d").date()
            if rec_date == today:
                summary["contacts"] += record.get("contact_count", 0)
                summary["meetings"] += record.get("meeting_count", 0)
                summary["tasks_completed"] += record.get("completed_tasks", 0)
                summary["revenue_potential"] += record.get("potential_revenue", 0.0)
    if not summary:
        return {"contacts": 0, "meetings": 0, "tasks_completed": 0, "revenue_potential": 0.0}
    avg_daily_contacts = summary["contacts"] / max(1, len(data))
    total_history_days = (today - datetime.date.min).days if data else 1
    daily_avg_revenue = summary["revenue_potential"] / max(1, total_history_days)
    return {**summary, "avg_daily_contacts": round(avg_daily_contacts, 2), "daily_avg_revenue": round(daily_avg_revenue, 2)}
