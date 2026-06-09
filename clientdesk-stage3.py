# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ClientDesk
def validate_contact_name(name):
    if not name or len(name.strip()) < 2:
        raise ValueError("Contact name must be at least 2 characters long.")
    return name.strip()

def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    return email.strip().lower()

def validate_phone(phone):
    cleaned = phone.replace(' ', '').replace('-', '').replace('+', '')
    if len(cleaned) < 10:
        raise ValueError("Phone number must be at least 10 digits.")
    return cleaned

def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def validate_task_description(desc):
    if not desc or len(desc.strip()) > 500:
        raise ValueError("Task description is required and must be under 500 characters.")
    return desc.strip()

def validate_identifier(identifier, prefix='ID'):
    if not identifier or not re.match(r'^[a-zA-Z0-9_-]+$', identifier):
        raise ValueError(f"Identifier '{identifier}' contains invalid characters or is empty.")
    return f"{prefix}_{identifier}"
