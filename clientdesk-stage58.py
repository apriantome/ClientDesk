# === Stage 58: Add bulk update behavior for selected records ===
# Project: ClientDesk
from typing import List, Dict, Any
def bulk_update_records(records: List[Dict[str, Any]], updates: Dict[str, Any], db_path: str = "clients.db") -> int:
    """Update multiple records with common fields and return count of modified rows."""
    try:
        import sqlite3
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        affected_count = 0
        for record in records:
            client_id = record.get("id")
            if not client_id:
                continue
            update_fields = {k: v for k, v in updates.items() if v is not None}
            set_clause = ", ".join(f"{col} = ?" for col in update_fields.keys())
            values = list(updates.values()) + [client_id]
            query = f"UPDATE clients SET {set_clause} WHERE id = ?"
            cursor.execute(query, values)
            if cursor.rowcount > 0:
                affected_count += 1
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during bulk update: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    return affected_count
