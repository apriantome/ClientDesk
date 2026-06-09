# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ClientDesk
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Contact:
    name: str
    phone: str
    email: Optional[str] = None
    notes: str = ""


@dataclass
class Meeting:
    title: str
    client_name: str
    scheduled_date: date
    duration_minutes: int = 30
    status: str = "scheduled"
    notes: str = ""


@dataclass
class Task:
    description: str
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    priority: int = 1
    completed: bool = False


@dataclass
class ClientHistoryEntry:
    date: date
    event_type: str  # "meeting", "call", "email"
    description: str
    related_contact_name: Optional[str] = None
