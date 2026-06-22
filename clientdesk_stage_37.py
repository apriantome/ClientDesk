# === Stage 37: Add recommendations for the next useful action ===
# Project: ClientDesk
from datetime import datetime, timedelta
import random

def get_next_action(client_name: str, last_contact_date: datetime) -> dict:
    days_since = (datetime.now() - last_contact_date).days
    if days_since == 0:
        return {"action": "Follow up immediately", "priority": "high", "reason": "Contact made today"}
    elif days_since <= 3:
        return {"action": "Send thank you note or quick check-in", "priority": "medium", "reason": f"Recent contact ({days_since}d ago)"}
    elif days_since <= 7:
        return {"action": "Share relevant industry news or resource", "priority": "low", "reason": "Keep engagement warm"}
    elif days_since <= 14:
        return {"action": "Ask about project progress or new needs", "priority": "medium", "reason": f"Two weeks since last contact ({days_since}d ago)"}
    else:
        return {
            "action": "Schedule a discovery call or send value-add content", 
            "priority": "high", 
            "reason": f"Long gap detected ({days_since}d ago). Re-engage."
        }

def generate_random_task(client_name: str) -> dict:
    tasks = [
        {"title": "Prepare proposal for {name}", "due_date": datetime.now() + timedelta(days=3)},
        {"title": "Call {name} to discuss timeline", "due_date": datetime.now() + timedelta(hours=24)},
        {"title": "Send contract draft to {name}", "due_date": datetime.now() + timedelta(days=5)},
    ]
    return random.choice(tasks).copy().format(name=client_name)

def analyze_history(client_id: int, history_list: list[dict]) -> dict | None:
    if not history_list:
        return {"action": "Create initial contact record", "priority": "critical"}
    
    recent_interactions = [h for h in history_list if (datetime.now() - datetime.fromisoformat(h.get('timestamp', ''))).days <= 30]
    if len(recent_interactions) < 2:
        return {"action": "Log a new interaction to build context", "priority": "medium"}
    
    last_interaction = recent_interactions[-1].get('type')
    if last_interaction == 'meeting':
        return {"action": "Send meeting notes and next steps summary", "priority": "high"}
    elif last_interaction in ['email', 'call']:
        return {"action": "Prepare follow-up email or call script", "priority": "low"}
    
    return None
