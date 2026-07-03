# === Stage 63: Add relationships between records where useful ===
# Project: ClientDesk
from typing import Optional, List
import datetime as dt

class Relationship:
    def __init__(self, type_: str = "contact", name: str = "", value: str = ""):
        self.type_ = type_
        self.name = name
        self.value = value
    
    @classmethod
    def from_contact(cls, contact: 'Contact') -> 'Relationship':
        return cls(type_="contact", name=contact.full_name, value=contact.phone)

class MeetingWithRelations(Meeting):
    def __init__(self, title: str, date: dt.date, attendees: List[Contact], notes: str = ""):
        super().__init__(title=title, date=date, notes=notes)
        self.attendees = attendees
    
    @property
    def attendee_names(self) -> List[str]:
        return [a.full_name for a in self.attendees]

class TaskWithRelations(Task):
    def __init__(self, title: str, due_date: dt.date, assignee: Optional[Contact], notes: str = ""):
        super().__init__(title=title, due_date=due_date, notes=notes)
        self.assignee = assignee
    
    @property
    def assigned_to(self) -> Optional[str]:
        return self.assignee.full_name if self.assignee else None

class ClientWithRelations(Client):
    def __init__(self, name: str, phone: str, email: str, company: str = ""):
        super().__init__(name=name, phone=phone, email=email)
        self.company = company
    
    @property
    def full_name(self) -> str:
        return f"{self.name} ({self.company})"

class HistoryEntryWithRelations(HistoryEntry):
    def __init__(self, client: Client, action_type: str, description: str, date: dt.date):
        super().__init__(client=client, action_type=action_type, description=description, date=date)
    
    @property
    def related_contact(self) -> Optional[Contact]:
        return self.client.contact if hasattr(self.client, 'contact') else None
