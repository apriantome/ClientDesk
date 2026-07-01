# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ClientDesk
class BulkDeleteGuard:
    def __init__(self, db):
        self.db = db
        self.confirm_flag = False

    def set_confirm(self, enabled: bool) -> None:
        """Enable or disable bulk delete confirmation."""
        self.confirm_flag = enabled

    async def execute_bulk_delete(
        self,
        table_name: str,
        condition: dict | None = None,
        limit: int = 0
    ) -> int:
        """Delete records with optional confirmation check and row count return."""
        if not self.confirm_flag:
            raise PermissionError("Bulk delete is disabled. Set confirm flag first.")

        query = f"DELETE FROM {table_name}"
        params = []
        if condition:
            where_parts = [f"{k} = %s" for k in condition.keys()]
            query += " WHERE " + " AND ".join(where_parts)
            params.extend(condition.values())

        async with self.db.cursor() as cursor:
            await cursor.execute(query, params)
            return await cursor.rowcount
