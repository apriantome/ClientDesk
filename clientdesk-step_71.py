# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ClientDesk
def seed_demo_data(db):
    """Insert deterministic sample contacts, meetings, tasks and history rows."""
    import datetime as dt
    now = dt.datetime.now()
    db.session.execute(
        db.text("INSERT INTO contacts (name, email, phone) VALUES (:n,:e,:p)"),
        [
            ("Alice Chen", "alice@example.com", "+1-555-0101"),
            ("Bob Smith",  "bob@example.com",  "+1-555-0202"),
            ("Carol Lee",  "carol@example.com","+1-555-0303"),
        ],
    )
    db.session.execute(
        db.text("INSERT INTO meetings (client_id, title, start_time, end_time) VALUES (:cid,:t,:s,:e)"),
        [
            (1, "Onboarding Call", now - dt.timedelta(days=2), now - dt.timedelta(hours=3)),
            (2, "Project Kickoff", now - dt.timedelta(days=5), now - dt.timedelta(days=4, hours=6)),
            (3, "Quarterly Review", now + dt.timedelta(days=10), now + dt.timedelta(days=10, hours=2)),
        ],
    )
    db.session.execute(
        db.text("INSERT INTO tasks (client_id, title, status) VALUES (:cid,:t,:s)"),
        [
            (1, "Send welcome email",     "done"),
            (1, "Set up training account","in_progress"),
            (2, "Draft SOW",             "pending"),
            (3, "Book venue",           "done"),
        ],
    )
    db.session.execute(
        db.text("INSERT INTO history (client_id, note) VALUES (:cid,:n)"),
        [
            (1, "Client requested training on Friday."),
            (2, "SOW draft sent for review."),
            (3, "Venue confirmed for next month."),
        ],
    )
