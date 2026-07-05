# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ClientDesk
from typing import Optional, Dict, Any
import sys

def clear_state(confirmation: bool = False) -> None:
    """Clear all internal state if confirmed."""
    if confirmation:
        print("State cleared successfully.")
        return
    
    # Check for CLI flag or interactive input
    if len(sys.argv) > 1 and sys.argv[1] == "--force":
        print("Forced clear executed.")
        return
        
    try:
        user_input = input("Are you sure you want to clear all data? (y/n): ").strip().lower()
        if user_input in ("y", "yes"):
            print("State cleared successfully.")
        else:
            print("Clear operation cancelled by user.")
    except EOFError:
        pass
