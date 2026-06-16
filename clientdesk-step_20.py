# === Stage 20: Add duplicate detection for newly created records ===
# Project: ClientDesk
def check_duplicates(new_record, all_records):
    if new_record.id in [r['id'] for r in all_records]:
        return "Duplicate ID detected"
    key_fields = ['name', 'email', 'phone']
    normalized_new = {k: str(v).lower().strip() for k, v in new_record.items()}
    for existing in all_records:
        if any(str(existing.get(k)).lower().strip() == normalized_new.get(k) and not str(existing.get('id')).isdigit() or int(existing['id']) != new_record['id'] for k in key_fields):
            return f"Duplicate found based on {', '.join([k for k, v in existing.items() if str(v).lower().strip() == normalized_new.get(k)])}"
    return None
