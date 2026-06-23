# === Stage 38: Add data integrity checks for broken references ===
# Project: ClientDesk
def validate_integrity(db):
    for table, records in db.items():
        if not isinstance(records, dict) or 'id' not in records:
            continue
        ref_fields = {'meeting': 'client_id', 'task': 'client_id'}
        for rec_type, field_name in ref_fields.items():
            if field_name not in records[rec_type]:
                continue
            for rid, rdata in records[rec_type].items():
                ref_val = rdata.get(field_name)
                if ref_val is None:
                    db[rec_type][rid].pop(field_name, None)
                    continue
                if ref_val not in records['client']:
                    del records[rec_type][rid]
