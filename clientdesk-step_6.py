# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ClientDesk
def delete_contact(contact_id, confirm=False):
    if not confirm:
        print(f"Contact {contact_id} deletion cancelled (confirmation required).")
        return False
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        if contact_id in contacts:
            del contacts[contact_id]
            with open("contacts.json", "w") as f:
                json.dump(contacts, f, indent=2)
            print(f"Contact {contact_id} deleted successfully.")
            return True
        else:
            print(f"Contact {contact_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting contact: {e}")
        return False

def delete_meeting(meeting_id, confirm=False):
    if not confirm:
        print(f"Meeting {meeting_id} deletion cancelled (confirmation required).")
        return False
    try:
        with open("meetings.json", "r") as f:
            meetings = json.load(f)
        if meeting_id in meetings:
            del meetings[meeting_id]
            with open("meetings.json", "w") as f:
                json.dump(meetings, f, indent=2)
            print(f"Meeting {meeting_id} deleted successfully.")
            return True
        else:
            print(f"Meeting {meeting_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting meeting: {e}")
        return False

def delete_task(task_id, confirm=False):
    if not confirm:
        print(f"Task {task_id} deletion cancelled (confirmation required).")
        return False
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        if task_id in tasks:
            del tasks[task_id]
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=2)
            print(f"Task {task_id} deleted successfully.")
            return True
        else:
            print(f"Task {task_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False

def delete_history_entry(entry_id, confirm=False):
    if not confirm:
        print(f"History entry {entry_id} deletion cancelled (confirmation required).")
        return False
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
        if entry_id in history:
            del history[entry_id]
            with open("history.json", "w") as f:
                json.dump(history, f, indent=2)
            print(f"History entry {entry_id} deleted successfully.")
            return True
        else:
            print(f"History entry {entry_id} not found.")
            return False
    except Exception as e:
        print(f"Error deleting history entry: {e}")
        return False
