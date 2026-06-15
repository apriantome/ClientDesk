# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ClientDesk
class DryRunContext:
    def __init__(self, dry_run=False):
        self._dry_run = dry_run
        self.changes = []

    @property
    def is_dry_run(self):
        return self._dry_run

    def record_change(self, action, entity_id, details=None):
        if not self.is_dry_run:
            return False
        entry = {"action": action, "entity_id": entity_id}
        if details:
            entry["details"] = details
        self.changes.append(entry)
        print(f"[DRY-RUN] {action}: {entity_id} - {details}")
        return True

    def commit(self):
        pass  # No-op in dry-run mode, changes are only logged
