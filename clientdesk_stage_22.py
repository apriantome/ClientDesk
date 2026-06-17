# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ClientDesk
from typing import Optional, List
import json
from datetime import datetime

def manage_favorites(db_path: str = "clients.json") -> None:
    """Add favorites and list them quickly."""
    data = load_data(db_path) or {"contacts": [], "favorites": []}
    
    def toggle_favorite(contact_id: int, is_favorite: bool) -> None:
        contact = next((c for c in data["contacts"] if c["id"] == contact_id), None)
        if not contact: return
        
        old_status = contact.get("is_favorite", False)
        if old_status != is_favorite:
            contact["is_favorite"] = is_favorite
            
            # Update history log
            action = "added to favorites" if is_favorite else "removed from favorites"
            data.setdefault("history", []).append({
                "type": "favorite_change",
                "contact_id": contact_id,
                "action": action,
                "timestamp": datetime.now().isoformat()
            })
            
    def get_favorites() -> List[dict]:
        return [c for c in data["contacts"] if c.get("is_favorite")]

def add_to_favorites(contact_id: int) -> Optional[str]:
    """Add a contact to favorites."""
    toggle_favorite(contact_id, True)
    save_data(data)
    favs = get_favorites()
    return f"Added {contact_id} to favorites. Total: {len(favs)}"

def remove_from_favorites(contact_id: int) -> Optional[str]:
    """Remove a contact from favorites."""
    toggle_favorite(contact_id, False)
    save_data(data)
    favs = get_favorites()
    return f"Removed {contact_id} from favorites. Total: {len(favs)}"

def list_favorites(db_path: str = "clients.json") -> List[dict]:
    """Return a list of favorite contacts."""
    data = load_data(db_path) or {"contacts": []}
    return get_favorites()
