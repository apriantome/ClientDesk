# === Stage 60: Add saved views for frequently used filters ===
# Project: ClientDesk
class SavedViewManager:
    def __init__(self, db):
        self.db = db
    
    def save_view(self, name, filters=None, sort_by='created_at', order='desc'):
        if filters is None:
            filters = {}
        query = "INSERT INTO saved_views (name, filters_json, sort_by, order) VALUES (%s, %s, %s, %s)"
        self.db.execute(query, (name, json.dumps(filters), sort_by, order))

    def get_saved_view(self, name):
        cursor = self.db.cursor()
        query = "SELECT filters_json, sort_by, order FROM saved_views WHERE name=%s"
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        if row:
            return {
                'filters': json.loads(row[0]),
                'sort_by': row[1],
                'order': row[2]
            }
        return None

    def apply_saved_view(self, name):
        view = self.get_saved_view(name)
        if not view:
            raise ValueError(f"Saved view '{name}' not found")
        
        filters = view['filters']
        sort_by = view['sort_by']
        order = view['order']

        conditions = []
        params = []
        for key, value in filters.items():
            if isinstance(value, dict):
                op = list(value.keys())[0]
                val = list(value.values())[0]
                conditions.append(f"{key} {op} %s")
                params.append(val)
            else:
                conditions.append(f"{key}=%s")
                params.append(value)

        condition_str = " AND ".join(conditions) if conditions else ""
        
        query = f"SELECT * FROM clients WHERE {condition_str} ORDER BY {sort_by} {order}"
        return self.db.fetch_all(query, tuple(params))
