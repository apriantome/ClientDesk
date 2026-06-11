# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ClientDesk
def update_contact(client_id, field_name, new_value):
    """Update a specific field for a contact. Returns updated dict or None if not found."""
    contacts = get_contacts()
    if client_id not in contacts:
        return None
    record = contacts[client_id]
    if field_name not in record:
        return None
    record[field_name] = new_value
    save_contacts(contacts)
    return record

def update_meeting(client_id, meeting_id, field_name, new_value):
    """Update a specific field for a meeting. Returns updated dict or None if not found."""
    meetings = get_meetings()
    key = f"{client_id}_{meeting_id}"
    if key not in meetings:
        return None
    record = meetings[key]
    if field_name not in record:
        return None
    record[field_name] = new_value
    save_meetings(meetings)
    return record

def update_task(client_id, task_id, field_name, new_value):
    """Update a specific field for a task. Returns updated dict or None if not found."""
    tasks = get_tasks()
    key = f"{client_id}_{task_id}"
    if key not in tasks:
        return None
    record = tasks[key]
    if field_name not in record:
        return None
    record[field_name] = new_value
    save_tasks(tasks)
    return record

def update_history_entry(client_id, entry_id, field_name, new_value):
    """Update a specific field for a history entry. Returns updated dict or None if not found."""
    history = get_history()
    key = f"{client_id}_{entry_id}"
    if key not in history:
        return None
    record = history[key]
    if field_name not in record:
        return None
    record[field_name] = new_value
    save_history(history)
    return record
