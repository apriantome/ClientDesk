# === Stage 28: Add overdue item detection based on due dates ===
# Project: ClientDesk
def check_overdue_items():
    overdue = []
    today = datetime.date.today()
    for client in clients:
        if hasattr(client, 'meetings') and client.meetings:
            for meeting in client.meetings:
                due_date = datetime.datetime.strptime(meeting['date'], '%Y-%m-%d').date()
                if due_date < today and not meeting.get('completed', False):
                    overdue.append({
                        'client_name': client.name,
                        'meeting_type': meeting.get('type', 'General'),
                        'days_overdue': (today - due_date).days,
                        'message': f"Meeting for {client.name} ({meeting['type']}) was scheduled for {meeting['date']} and is now overdue."
                    })
    if overdue:
        print(f"\n⚠️  Overdue items detected:")
        for item in overdue:
            print(f"- {item['message']} (Overdue by {item['days_overdue']} days)")
        return True
    return False
