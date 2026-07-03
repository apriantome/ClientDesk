# === Stage 64: Add validation for relationship references ===
# Project: ClientDesk
class RelationshipValidator:
    def __init__(self, db):
        self.db = db

    def validate_meeting(self, meeting_data):
        client_id = meeting_data.get('client_id')
        if not self._exists_in_contacts(client_id):
            raise ValueError(f"Meeting references non-existent client {client_id}")
        return True

    def validate_task(self, task_data):
        client_id = task_data.get('client_id')
        if not self._exists_in_contacts(client_id):
            raise ValueError(f"Task references non-existent client {client_id}")
        return True

    def _exists_in_contacts(self, contact_id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id FROM contacts WHERE id = %s", (contact_id,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
