# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ClientDesk
def parse_date_input(raw: str) -> datetime.date | None:
    """Parse date from string with clear error messages."""
    if not raw.strip():
        return None
    formats = [("%Y-%m-%d", "%d.%m.%Y"), ("%Y/%m/%d", "%d/%m/%Y")]
    for fmt, alt in formats:
        try:
            return datetime.strptime(raw.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты '{raw}'. Используйте YYYY-MM-DD или DD.MM.YYYY.")
