# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ClientDesk
class PriorityCalculator:
    def __init__(self, client):
        self.client = client
    
    def calculate_score(self):
        score = 0
        if self.client.last_contact_days < 7:
            score += 30
        elif self.client.last_contact_days < 14:
            score += 20
        
        urgent_tasks = sum(1 for t in self.client.tasks.values() 
                          if not t.completed and (t.deadline - datetime.now()).days <= 2)
        score += urgent_tasks * 25
        
        upcoming_meetings = sum(1 for m in self.client.meetings.values() 
                               if m.date > datetime.now().date() and (m.date - datetime.now().date()).days <= 3)
        score += upcoming_meetings * 40
        
        return min(score, 100)

    def get_priority_label(self):
        score = self.calculate_score()
        if score >= 80:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        elif score >= 25:
            return "MEDIUM"
        else:
            return "LOW"
