# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ClientDesk
class ActivityLog:
    def __init__(self, storage):
        self.storage = storage
    
    def log(self, action_name: str, details: dict = None) -> bool:
        try:
            entry = {
                "timestamp": datetime.now().isoformat(),
                "action": action_name,
                "details": details or {}
            }
            self.storage["history"].append(entry)
            return True
        except Exception as e:
            print(f"Log error: {e}")
            return False
    
    def get_recent(self, limit: int = 10) -> list:
        history = self.storage.get("history", [])
        return history[-limit:] if len(history) >= limit else history[:]
