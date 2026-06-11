# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ClientDesk
class ClientDeskFormatter:
    def __init__(self, width=80):
        self.width = width

    def format_table(self, headers, rows):
        if not rows:
            return ""
        col_widths = [max(len(str(h)), max((len(str(r)) for r in rows), default=0)) for h in headers]
        lines = []
        header_line = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        lines.append(header_line)
        separator = "+".join("-" * (col_widths[i] + 2) for i in range(len(headers)))
        lines.append(separator)
        for row in rows:
            line = "  ".join(str(row.get(h, "")).ljust(col_widths[i]) if h in row else "" for i, h in enumerate(headers))
            lines.append(line)
        return "\n".join(lines)

    def format_contact(self, contact):
        name = contact.get("name", "N/A")
        phone = contact.get("phone", "")
        email = contact.get("email", "")
        tags = ", ".join(contact.get("tags", [])) if isinstance(contact.get("tags"), list) else ""
        return f"[{name}]\n  Phone: {phone}\n  Email: {email}\n  Tags: {tags}"

    def format_task(self, task):
        title = task.get("title", "No Title")
        status = task.get("status", "Pending")
        due = task.get("due_date", "")
        priority = task.get("priority", "Normal")
        desc = task.get("description", "")
        lines = [f"Task: {title} [{status}]"]
        if priority:
            lines.append(f"  Priority: {priority}")
        if due:
            lines.append(f"  Due: {due}")
        if desc:
            lines.append(f"  Description: {desc}")
        return "\n".join(lines)

    def format_meeting(self, meeting):
        title = meeting.get("title", "No Title")
        date = meeting.get("date", "")
        time = meeting.get("time", "")
        attendees = ", ".join(meeting.get("attendees", [])) if isinstance(meeting.get("attendees"), list) else ""
        notes = meeting.get("notes", "")
        lines = [f"Meeting: {title}"]
        if date and time:
            lines.append(f"  Date/Time: {date} {time}")
        elif date:
            lines.append(f"  Date: {date}")
        elif time:
            lines.append(f"  Time: {time}")
        if attendees:
            lines.append(f"  Attendees: {attendees}")
        if notes:
            lines.append(f"  Notes: {notes}")
        return "\n".join(lines)

    def format_history_entry(self, entry):
        date = entry.get("date", "")
        action = entry.get("action", "")
        details = entry.get("details", "")
        return f"[{date}] {action}: {details}"
