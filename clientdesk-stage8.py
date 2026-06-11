# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ClientDesk
class FilterManager:
    def __init__(self, records):
        self.records = records

    def filter_records(self, status=None, category=None, owner=None, tag=None):
        filtered = self.records.copy()
        if status:
            filtered = [r for r in filtered if r.get('status') == status]
        if category:
            filtered = [r for r in filtered if r.get('category') == category]
        if owner:
            filtered = [r for r in filtered if r.get('owner') == owner]
        if tag:
            filtered = [r for r in filtered if r.get('tag') == tag]
        return filtered

    def apply_filters(self, **kwargs):
        return self.filter_records(**kwargs)
