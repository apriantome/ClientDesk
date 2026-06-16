# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ClientDesk
import os, json, shutil
from datetime import datetime, timedelta
ARCHIVE_DIR = "archive"
def archive_completed():
    if not os.path.exists(ARCHIVE_DIR): os.makedirs(ARCHIVE_DIR)
    for f in ["contacts.json", "meetings.json", "tasks.json"]:
        src = f"data/{f}"
        dst = f"{ARCHIVE_DIR}/{datetime.now().strftime('%Y-%m-%d')}-{f}"
        if os.path.exists(src): shutil.move(src, dst)

def restore_from_archive():
    for f in ["contacts.json", "meetings.json", "tasks.json"]:
        srcs = [os.path.join(ARCHIVE_DIR, x) for x in os.listdir(ARCHIVE_DIR)]
        for s in sorted(srcs):
            if f in s: shutil.move(s, f"data/{f}")
