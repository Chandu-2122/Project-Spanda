# memory/reflection_memory.py
import json
import os

class ReflectionMemory:
    """
    Optional long-term reflection storage.
    Fully user-controlled.
    Persists only one session at a time.
    """

    FILE_PATH = "reflection_session.json"

    def __init__(self):
        self.sessions = []

        # Remove old session if exists
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)

    def add(self, entry: dict):
        """Add a new reflection entry and persist to file."""
        self.sessions.append(entry)
        self._save_to_disk()

    def _save_to_disk(self):
        """Save sessions to JSON file."""
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(self.sessions, f, indent=2)
        except Exception as e:
            print(f"[ReflectionMemory ERROR] Could not save: {e}")

    def list_summaries(self):
        return [session.get("summary", "") for session in self.sessions]

    def get_last_summary(self):
        """Return last session summary if exists."""
        if self.sessions:
            return self.sessions[-1].get("summary", "")
        return ""
