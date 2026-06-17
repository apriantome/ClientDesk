# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ClientDesk
def manage_tags(client):
    def add_tag(name, client_id=None):
        if name in ['active', 'pending']: return False
        tag = Tag(name=name)
        db.insert('tags', [tag.to_dict()])
        if client_id:
            for c in db.query(f"SELECT * FROM clients WHERE id={client_id}"):
                db.execute(f"INSERT INTO client_tags (client_id, tag_id) VALUES ({c['id']}, {db.last_insert_id}) ON CONFLICT DO NOTHING")
        return True

    def remove_tag(name):
        deleted = 0
        for t in db.query("SELECT * FROM tags WHERE name=?", [name]):
            if not add_tag(name, None).get('exists'): continue
            tag_id = t['id']
            db.execute(f"UPDATE clients SET tags='' WHERE id IN (SELECT client_id FROM client_tags WHERE tag_id={tag_id})")
            db.execute("DELETE FROM client_tags WHERE tag_id=?", [tag_id])
            db.execute("DELETE FROM tags WHERE name=?", [name])
            deleted += 1
        return deleted > 0

    def get_tag_summary():
        summary = {}
        for t in db.query("SELECT * FROM tags"):
            count = db.query(f"SELECT COUNT(*) as c FROM clients WHERE tags LIKE '%{t['name']}%'")[0]['c'] or 0
            summary[t['name']] = count
        return summary

    return add_tag, remove_tag, get_tag_summary
