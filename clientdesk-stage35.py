# === Stage 35: Add active user switching and user-specific records ===
# Project: ClientDesk
class UserManager:
    def __init__(self, db):
        self.db = db
        self.active_user_id = None
    
    def set_active(self, user_id):
        if not user_id.isdigit():
            return False
        self.active_user_id = int(user_id)
        return True
    
    def get_current_records(self, record_type='contacts'):
        prefix = f"{record_type}_"
        records = []
        for key in self.db:
            if key.startswith(prefix):
                data = self.db[key]
                user_str = str(data.get('user_id', ''))
                if not self.active_user_id or user_str == str(self.active_user_id):
                    records.append({**data, 'id': key})
        return sorted(records, key=lambda x: x.get('date_added', 0), reverse=True)
