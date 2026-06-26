# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ClientDesk
from datetime import date, timedelta
import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email)) and len(email) <= 254

def validate_phone(phone: str) -> bool:
    cleaned = re.sub(r'[^\d]', '', phone)
    return len(cleaned) in (10, 11, 13, 14)

def is_valid_date(d_str: str) -> bool:
    try:
        date.fromisoformat(d_str)
        return True
    except ValueError:
        return False

class ClientValidator:
    def __init__(self):
        self.errors = []

    def validate_contact(self, email: str, phone: str) -> list[str]:
        if not validate_email(email):
            self.errors.append("Invalid email format")
        if not validate_phone(phone):
            self.errors.append("Invalid phone number length or characters")
        return self.errors.copy()

    def clear_errors(self):
        self.errors.clear()
