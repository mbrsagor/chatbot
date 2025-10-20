# app/storage.py
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

LOG_PATH = Path("conversations.json")

def append_message(session_id: str, sender: str, message: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session": session_id,
        "sender": sender,
        "message": message
    }
    logs = []
    if LOG_PATH.exists():
        try:
            logs = json.loads(LOG_PATH.read_text())
        except Exception:
            logs = []
    logs.append(entry)
    LOG_PATH.write_text(json.dumps(logs, indent=2))

