# === Stage 19: Add undo support for the last simple mutation ===
# Project: ClientDesk
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class UndoStack:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
    
    def push(self, action_type: str, data: Dict[str, Any]):
        self.history.append({
            "type": action_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        })
    
    def undo_last(self) -> Optional[Dict[str, Any]]:
        if not self.history:
            return None
        last_action = self.history.pop()
        return last_action

# Usage example for ClientDesk mutation
def perform_mutation_with_undo(stack: UndoStack, action_type: str, data: Dict[str, Any]):
    stack.push(action_type, data)
