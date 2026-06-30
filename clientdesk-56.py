# === Stage 56: Add compact error classes for domain failures ===
# Project: ClientDesk
class ClientDeskError(Exception): pass
class ContactNotFoundError(ClientDeskError): pass
class MeetingConflictError(ClientDeskError): pass
class TaskInvalidDateError(ClientDeskError): pass
class HistoryCorruptionError(ClientDeskError): pass
class InvalidContactFormatError(ClientDeskError): pass
class DuplicateMeetingIdError(ClientDeskError): pass
class UnauthorizedAccessError(ClientDeskError): pass
