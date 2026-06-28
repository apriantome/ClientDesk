# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ClientDesk
def format_date(date_str):
    """Convert ISO date string to localized Russian format."""
    from datetime import datetime
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    return dt.strftime("%d.%m.%Y")

def truncate_text(text, max_len=50):
    """Truncate text with ellipsis if it exceeds the maximum length."""
    return (text[:max_len] + "…") if len(text) > max_len else text

def safe_get(d, *keys, default=None):
    """Safely retrieve a nested dictionary value without raising KeyError."""
    for key in keys:
        d = d.get(key, {})
    return d if isinstance(d, dict) and not isinstance(d, str) else (d if d is not None else default)

def calculate_days_diff(start_date_str, end_date_str):
    """Calculate the number of days between two ISO date strings."""
    from datetime import datetime
    start = datetime.fromisoformat(start_date_str.replace('Z', '+00:00').date())
    end = datetime.fromisoformat(end_date_str.replace('Z', '+00:00').date())
    return (end - start).days

def generate_task_id(prefix="TASK", counter=1):
    """Generate a unique task identifier based on prefix and current counter."""
    import uuid
    short_uuid = uuid.uuid4().hex[:8].upper()
    return f"{prefix}-{short_uuid}"
