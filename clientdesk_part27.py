# === Stage 27: Add monthly summary calculations ===
# Project: ClientDesk
def calculate_monthly_summary(records):
    from datetime import datetime, timedelta
    now = datetime.now()
    current_month = (now.year, now.month)
    summary = {"contacts": 0, "meetings_held": 0, "tasks_completed": 0, "revenue_estimate": 0}
    for r in records:
        if isinstance(r.get("type"), str):
            t = r["type"].lower()
            date_str = r.get("date", "")
            try:
                dt = datetime.strptime(date_str[:10], "%Y-%m-%d")
                record_month = (dt.year, dt.month)
            except ValueError:
                continue
            if current_month == record_month:
                if t in ("contact_added", "new_client"):
                    summary["contacts"] += 1
                elif t in ("meeting_scheduled", "meeting_held"):
                    summary["meetings_held"] += 1
                elif t in ("task_completed", "deal_closed"):
                    summary["tasks_completed"] += 1
                    if r.get("value") and isinstance(r["value"], (int, float)):
                        summary["revenue_estimate"] += int(r["value"])
    return summary
